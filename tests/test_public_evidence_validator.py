from __future__ import annotations

import json
import subprocess
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.validate_public_evidence import REPO_ROOT, ValidationError, validate


class PublicEvidenceValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.repo_copy = Path(self.temp_dir.name) / "repo"
        shutil.copytree(REPO_ROOT, self.repo_copy, ignore=shutil.ignore_patterns(".git", "__pycache__"))
        self.tracked_files = subprocess.run(
            ["git", "ls-files", "-z"],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.split("\0")
        self.tracked_files = [item for item in self.tracked_files if item]

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_committed_evidence_set_passes(self) -> None:
        result = validate(self.repo_copy, tracked_files=self.tracked_files)
        self.assertEqual(result.json_examples, 2)

    def test_collects_tracked_files_from_git_in_production(self) -> None:
        calls: list[list[str]] = []

        def fake_git_runner(command: list[str], repo_root: Path) -> bytes:
            calls.append(command)
            self.assertEqual(repo_root, self.repo_copy)
            return b"README.md\0docs/architecture.md\0"

        validate(self.repo_copy, git_runner=fake_git_runner)
        self.assertEqual(calls, [["git", "ls-files", "-z"]])

    def test_rejects_malformed_synthetic_json(self) -> None:
        target = self.repo_copy / "public-proof/examples/representative-operational-flow/synthetic-job.json"
        target.write_text("{not valid json")

        with self.assertRaisesRegex(ValidationError, "not valid JSON"):
            validate(self.repo_copy, tracked_files=self.tracked_files)

    def test_rejects_missing_manifest_reference(self) -> None:
        manifest = self.repo_copy / "public-proof/manifest/evidence-manifest.md"
        manifest.write_text(
            manifest.read_text().replace(
                "`public-proof/examples/representative-operational-flow/`",
                "`public-proof/examples/missing-flow/`",
                1,
            )
        )

        with self.assertRaisesRegex(ValidationError, "manifest reference"):
            validate(self.repo_copy, tracked_files=self.tracked_files)

    def test_rejects_deeply_nested_tracked_database(self) -> None:
        with self.assertRaisesRegex(ValidationError, "nested/archive/runtime.db"):
            validate(self.repo_copy, tracked_files=["nested/archive/runtime.db"])

    def test_rejects_nested_tracked_log_or_csv(self) -> None:
        with self.assertRaisesRegex(ValidationError, "nested/export/data.csv"):
            validate(self.repo_copy, tracked_files=["nested/export/data.csv"])

    def test_rejects_tracked_env_file(self) -> None:
        with self.assertRaisesRegex(ValidationError, "config/.env"):
            validate(self.repo_copy, tracked_files=["config/.env"])

    def test_untracked_prohibited_local_file_does_not_fail_validation(self) -> None:
        prohibited = self.repo_copy / "public-proof" / "runtime.log"
        prohibited.write_text("example")
        result = validate(self.repo_copy, tracked_files=["README.md"])
        self.assertEqual(result.checked_files, 15)

    def test_git_ls_files_failure_is_reported_clearly(self) -> None:
        def failing_git_runner(command: list[str], repo_root: Path) -> bytes:
            raise ValidationError("unable to obtain tracked files via git ls-files: git unavailable")

        with self.assertRaisesRegex(ValidationError, "git ls-files"):
            validate(self.repo_copy, git_runner=failing_git_runner)

    def test_ignored_local_bytecode_does_not_affect_validation(self) -> None:
        cache_dir = self.repo_copy / "scripts" / "__pycache__"
        cache_dir.mkdir()
        (cache_dir / "check.cpython-313.pyc").write_bytes(b"compiled")
        result = validate(self.repo_copy, tracked_files=["README.md"])
        self.assertEqual(result.json_examples, 2)

    def test_rejects_missing_synthetic_timestamp_note(self) -> None:
        target = self.repo_copy / "public-proof/examples/representative-operational-flow/lead-event-example.json"
        payload = json.loads(target.read_text())
        payload.pop("timestamp_note")
        target.write_text(json.dumps(payload, indent=2))

        with self.assertRaisesRegex(ValidationError, "missing required field\\(s\\): timestamp_note"):
            validate(self.repo_copy, tracked_files=self.tracked_files)


if __name__ == "__main__":
    unittest.main()
