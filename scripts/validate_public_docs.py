"""Validate tracked Markdown links for portability within the repository."""

from __future__ import annotations

import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Callable
from urllib.parse import urlsplit


REPO_ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"!?\[([^\]]*)\]\(([^)]+)\)")
FENCE_RE = re.compile(r"^```")
LOCAL_ABSOLUTE_PREFIXES = ("/Users/", "/home/", "/tmp/")
WINDOWS_DRIVE_RE = re.compile(r"^[A-Za-z]:[\\\\/]")


class ValidationError(Exception):
    """Raised when tracked Markdown validation fails."""


GitRunner = Callable[[list[str], Path], bytes]


@dataclass
class MarkdownValidationResult:
    checked_files: int


def validate_markdown_links(
    repo_root: Path = REPO_ROOT,
    *,
    tracked_files: list[str] | None = None,
    git_runner: GitRunner | None = None,
) -> MarkdownValidationResult:
    markdown_files = _collect_tracked_markdown_files(
        repo_root, tracked_files=tracked_files, git_runner=git_runner
    )
    errors: list[str] = []
    for rel_path in markdown_files:
        errors.extend(_validate_markdown_file(repo_root, rel_path))
    if errors:
        raise ValidationError("\n".join(errors))
    return MarkdownValidationResult(checked_files=len(markdown_files))


def main() -> int:
    try:
        result = validate_markdown_links()
    except ValidationError as exc:
        print(f"PUBLIC DOCS VALIDATION FAILED:\n{exc}", file=sys.stderr)
        return 1

    print(
        "PUBLIC DOCS VALIDATION PASSED: "
        f"{result.checked_files} tracked Markdown files checked."
    )
    return 0


def _collect_tracked_markdown_files(
    repo_root: Path,
    *,
    tracked_files: list[str] | None = None,
    git_runner: GitRunner | None = None,
) -> list[Path]:
    if tracked_files is None:
        runner = git_runner or _run_git_ls_files
        try:
            output = runner(["git", "ls-files", "-z", "--", "*.md"], repo_root)
        except ValidationError:
            raise
        except Exception as exc:
            raise ValidationError(f"unable to obtain tracked Markdown files via git ls-files: {exc}") from exc
        tracked_files = [item for item in output.decode("utf-8").split("\0") if item]

    return [Path(item.replace("\\", "/")) for item in tracked_files if item]


def _run_git_ls_files(command: list[str], repo_root: Path) -> bytes:
    completed = subprocess.run(command, cwd=repo_root, check=False, capture_output=True)
    if completed.returncode != 0:
        stderr = completed.stderr.decode("utf-8", errors="replace").strip()
        detail = f": {stderr}" if stderr else ""
        raise ValidationError(f"unable to obtain tracked Markdown files via git ls-files{detail}")
    return completed.stdout


def _validate_markdown_file(repo_root: Path, rel_path: Path) -> list[str]:
    errors: list[str] = []
    in_fence = False
    text = (repo_root / rel_path).read_text()
    for line_number, line in enumerate(text.splitlines(), start=1):
        if FENCE_RE.match(line.strip()):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for match in LINK_RE.finditer(line):
            destination = match.group(2).strip()
            problem = _validate_destination(repo_root, rel_path, destination)
            if problem is not None:
                errors.append(f"{rel_path}:{line_number}: {destination} - {problem}")
    return errors


def _validate_destination(repo_root: Path, rel_path: Path, destination: str) -> str | None:
    if not destination:
        return "empty destination"
    if destination.startswith("<") and destination.endswith(">"):
        destination = destination[1:-1].strip()
    if destination.startswith("file://"):
        return "file URI is not allowed"
    if destination.startswith(LOCAL_ABSOLUTE_PREFIXES):
        return "machine-local absolute path"
    if WINDOWS_DRIVE_RE.match(destination):
        return "Windows absolute path is not allowed"
    split = urlsplit(destination)
    if not split.scheme and not split.netloc and destination.startswith("#"):
        return None
    if split.scheme in {"http", "https", "mailto"}:
        return None
    if split.scheme and len(split.scheme) > 1:
        return None

    cleaned = destination.split("#", 1)[0].split("?", 1)[0].strip()
    if not cleaned:
        return None
    if cleaned.startswith("/"):
        return "repository-absolute paths are not allowed"

    base = PurePosixPath(rel_path.as_posix()).parent
    normalized = PurePosixPath(base, cleaned)
    normalized_parts: list[str] = []
    for part in normalized.parts:
        if part in {"", "."}:
            continue
        if part == "..":
            if normalized_parts:
                normalized_parts.pop()
                continue
            return "link escapes the repository"
        normalized_parts.append(part)

    candidate = repo_root.joinpath(*normalized_parts)
    if not candidate.exists():
        return "broken internal link"
    return None


if __name__ == "__main__":
    raise SystemExit(main())
