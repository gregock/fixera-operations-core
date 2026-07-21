from __future__ import annotations

import subprocess
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.validate_public_docs import ValidationError, validate_markdown_links
from scripts.validate_public_evidence import REPO_ROOT


class PublicDocsValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.repo_copy = Path(self.temp_dir.name) / "repo"
        shutil.copytree(REPO_ROOT, self.repo_copy, ignore=shutil.ignore_patterns(".git", "__pycache__"))
        self.markdown_files = subprocess.run(
            ["git", "ls-files", "-z", "--", "*.md"],
            cwd=REPO_ROOT,
            check=True,
            capture_output=True,
            text=True,
        ).stdout.split("\0")
        self.markdown_files = [item for item in self.markdown_files if item]

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_committed_repository_passes(self) -> None:
        result = validate_markdown_links(self.repo_copy, tracked_files=self.markdown_files)
        self.assertGreaterEqual(result.checked_files, 1)

    def test_valid_relative_file_link_passes(self) -> None:
        doc = self.repo_copy / "docs" / "guide.md"
        doc.write_text("[arch](../README.md)\n")
        validate_markdown_links(self.repo_copy, tracked_files=["docs/guide.md"])

    def test_valid_relative_directory_link_passes(self) -> None:
        doc = self.repo_copy / "docs" / "guide.md"
        doc.write_text("[examples](../public-proof/examples/representative-operational-flow/)\n")
        validate_markdown_links(self.repo_copy, tracked_files=["docs/guide.md"])

    def test_broken_relative_link_fails(self) -> None:
        doc = self.repo_copy / "docs" / "guide.md"
        doc.write_text("[missing](../missing.md)\n")
        with self.assertRaisesRegex(ValidationError, "broken internal link"):
            validate_markdown_links(self.repo_copy, tracked_files=["docs/guide.md"])

    def test_users_absolute_path_fails(self) -> None:
        doc = self.repo_copy / "docs" / "guide.md"
        doc.write_text("[bad](/Users/example/file.md)\n")
        with self.assertRaisesRegex(ValidationError, "machine-local absolute path"):
            validate_markdown_links(self.repo_copy, tracked_files=["docs/guide.md"])

    def test_file_uri_fails(self) -> None:
        doc = self.repo_copy / "docs" / "guide.md"
        doc.write_text("[bad](file:///tmp/file.md)\n")
        with self.assertRaisesRegex(ValidationError, "file URI"):
            validate_markdown_links(self.repo_copy, tracked_files=["docs/guide.md"])

    def test_windows_drive_path_fails(self) -> None:
        doc = self.repo_copy / "docs" / "guide.md"
        doc.write_text("[bad](C:/temp/file.md)\n")
        with self.assertRaisesRegex(ValidationError, "Windows absolute path"):
            validate_markdown_links(self.repo_copy, tracked_files=["docs/guide.md"])

    def test_repository_escaping_link_fails(self) -> None:
        doc = self.repo_copy / "docs" / "guide.md"
        doc.write_text("[bad](../../outside.md)\n")
        with self.assertRaisesRegex(ValidationError, "escapes the repository"):
            validate_markdown_links(self.repo_copy, tracked_files=["docs/guide.md"])

    def test_external_https_link_is_ignored(self) -> None:
        doc = self.repo_copy / "docs" / "guide.md"
        doc.write_text("[docs](https://example.com/docs)\n")
        validate_markdown_links(self.repo_copy, tracked_files=["docs/guide.md"])

    def test_fragment_only_link_is_ignored(self) -> None:
        doc = self.repo_copy / "docs" / "guide.md"
        doc.write_text("[jump](#section)\n")
        validate_markdown_links(self.repo_copy, tracked_files=["docs/guide.md"])

    def test_link_inside_fenced_code_block_is_ignored(self) -> None:
        doc = self.repo_copy / "docs" / "guide.md"
        doc.write_text("```\n[code](../../outside.md)\n```\n")
        validate_markdown_links(self.repo_copy, tracked_files=["docs/guide.md"])

    def test_git_failure_is_reported_clearly(self) -> None:
        def failing_git_runner(command: list[str], repo_root: Path) -> bytes:
            raise ValidationError("unable to obtain tracked Markdown files via git ls-files: git unavailable")

        with self.assertRaisesRegex(ValidationError, "git ls-files"):
            validate_markdown_links(self.repo_copy, git_runner=failing_git_runner)


if __name__ == "__main__":
    unittest.main()
