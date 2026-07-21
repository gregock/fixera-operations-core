from __future__ import annotations

import json
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

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_committed_evidence_set_passes(self) -> None:
        result = validate(self.repo_copy)
        self.assertEqual(result.json_examples, 2)

    def test_rejects_malformed_synthetic_json(self) -> None:
        target = self.repo_copy / "public-proof/examples/representative-operational-flow/synthetic-job.json"
        target.write_text("{not valid json")

        with self.assertRaisesRegex(ValidationError, "not valid JSON"):
            validate(self.repo_copy)

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
            validate(self.repo_copy)

    def test_rejects_prohibited_runtime_artifact(self) -> None:
        prohibited = self.repo_copy / "public-proof" / "runtime.log"
        prohibited.write_text("example")

        with self.assertRaisesRegex(ValidationError, "prohibited tracked artifact"):
            validate(self.repo_copy)

    def test_rejects_missing_synthetic_timestamp_note(self) -> None:
        target = self.repo_copy / "public-proof/examples/representative-operational-flow/lead-event-example.json"
        payload = json.loads(target.read_text())
        payload.pop("timestamp_note")
        target.write_text(json.dumps(payload, indent=2))

        with self.assertRaisesRegex(ValidationError, "missing required field\\(s\\): timestamp_note"):
            validate(self.repo_copy)


if __name__ == "__main__":
    unittest.main()
