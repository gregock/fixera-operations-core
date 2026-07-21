"""Validate the public evidence package for the portfolio repository."""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "case-study.md",
    "docs/architecture.md",
    "docs/workflows.md",
    "docs/safety-boundaries.md",
    "public-proof/README.md",
    "public-proof/diagrams/architecture-v1.md",
    "public-proof/diagrams/workflow-v1.md",
    "public-proof/manifest/evidence-manifest.md",
    "public-proof/examples/representative-operational-flow/README.md",
    "public-proof/examples/representative-operational-flow/provenance.md",
    "public-proof/examples/representative-operational-flow/validation.md",
    "public-proof/examples/representative-operational-flow/synthetic-job.json",
    "public-proof/examples/representative-operational-flow/lead-event-example.json",
    "tests/smoke/README.md",
]

JOB_REQUIRED_FIELDS = {
    "job_id",
    "source",
    "job_type",
    "customer_type",
    "lifecycle_state",
    "hours",
    "materials_cost",
    "job_price",
    "currency",
    "profit_analysis",
    "notes",
}

LEAD_REQUIRED_FIELDS = {
    "event_id",
    "event_type",
    "landing_page",
    "page_key",
    "source",
    "medium",
    "campaign",
    "cta_label",
    "timestamp_utc",
    "timestamp_note",
    "is_test",
    "is_internal",
    "notes",
}

PROHIBITED_PATTERNS = {
    ".db",
    ".sqlite",
    ".sqlite3",
    ".log",
    ".csv",
    ".tsv",
    ".sql",
    ".env",
}

MANIFEST_FILE_LINK_RE = re.compile(r"`([^`]+)`")


@dataclass
class ValidationResult:
    checked_files: int
    manifest_references: int
    json_examples: int


class ValidationError(Exception):
    """Raised when public evidence validation fails."""


def validate(repo_root: Path = REPO_ROOT) -> ValidationResult:
    _assert_required_files(repo_root)
    tracked = _collect_tracked_files(repo_root)
    _assert_no_prohibited_artifacts(tracked)
    _assert_manifest_references_exist(repo_root)
    _assert_json_examples(repo_root)
    _assert_internal_consistency(repo_root)
    return ValidationResult(
        checked_files=len(REQUIRED_FILES),
        manifest_references=_count_manifest_references(repo_root),
        json_examples=2,
    )


def main() -> int:
    try:
        result = validate()
    except ValidationError as exc:
        print(f"PUBLIC EVIDENCE VALIDATION FAILED: {exc}", file=sys.stderr)
        return 1

    print(
        "PUBLIC EVIDENCE VALIDATION PASSED: "
        f"{result.checked_files} required files, "
        f"{result.manifest_references} manifest references, "
        f"{result.json_examples} JSON examples."
    )
    return 0


def _assert_required_files(repo_root: Path) -> None:
    missing = [path for path in REQUIRED_FILES if not (repo_root / path).is_file()]
    if missing:
        raise ValidationError(f"missing required file(s): {', '.join(sorted(missing))}")


def _collect_tracked_files(repo_root: Path) -> list[Path]:
    files: list[Path] = []
    for path in repo_root.rglob("*"):
        if ".git" in path.parts:
            continue
        if path.is_file():
            files.append(path.relative_to(repo_root))
    return files


def _assert_no_prohibited_artifacts(tracked_files: list[Path]) -> None:
    violations = []
    for path in tracked_files:
        name = path.name.lower()
        if name == ".env" or name.endswith(".env"):
            violations.append(str(path))
            continue
        if any(name.endswith(pattern) for pattern in PROHIBITED_PATTERNS if pattern != ".env"):
            violations.append(str(path))
    if violations:
        raise ValidationError(
            "prohibited tracked artifact(s) present: " + ", ".join(sorted(violations))
        )


def _assert_manifest_references_exist(repo_root: Path) -> None:
    manifest = (repo_root / "public-proof/manifest/evidence-manifest.md").read_text()
    missing = []
    for ref in _manifest_paths(manifest):
        if ref.endswith("/"):
            if not (repo_root / ref).is_dir():
                missing.append(ref)
        elif not (repo_root / ref).exists():
            missing.append(ref)
    if missing:
        raise ValidationError(
            "manifest reference(s) missing from repository: " + ", ".join(sorted(missing))
        )


def _assert_json_examples(repo_root: Path) -> None:
    job = _load_json(repo_root / "public-proof/examples/representative-operational-flow/synthetic-job.json")
    lead = _load_json(
        repo_root / "public-proof/examples/representative-operational-flow/lead-event-example.json"
    )

    _assert_fields(job, JOB_REQUIRED_FIELDS, "synthetic-job.json")
    _assert_fields(lead, LEAD_REQUIRED_FIELDS, "lead-event-example.json")

    if not any("synthetic" in str(note).lower() for note in job.get("notes", [])):
        raise ValidationError("synthetic-job.json must include an explicit synthetic marker")
    if not any("synthetic" in str(note).lower() for note in lead.get("notes", [])):
        raise ValidationError("lead-event-example.json must include an explicit synthetic marker")

    profit = job["profit_analysis"]
    if profit.get("revenue") != job["job_price"]:
        raise ValidationError("synthetic-job.json revenue must match job_price")
    if profit.get("costs") != job["materials_cost"]:
        raise ValidationError("synthetic-job.json costs must match materials_cost")
    if profit.get("gross_margin") != profit.get("revenue", 0) - profit.get("costs", 0):
        raise ValidationError("synthetic-job.json gross_margin must equal revenue minus costs")

    timestamp_note = str(lead.get("timestamp_note", ""))
    if "synthetic" not in timestamp_note.lower() or "not tied to a real customer" not in timestamp_note.lower():
        raise ValidationError("lead-event-example.json must explain that timestamp_utc is synthetic")


def _assert_internal_consistency(repo_root: Path) -> None:
    validation_text = (
        repo_root / "public-proof/examples/representative-operational-flow/validation.md"
    ).read_text()
    if "synthetic and is not tied to a real customer or operational event" not in validation_text:
        raise ValidationError(
            "validation.md must state that any sample timestamp is synthetic and not tied to a real event"
        )

    readme_text = (repo_root / "README.md").read_text()
    if "public-safe architecture and system-design case study, not the deployable production backend" not in readme_text:
        raise ValidationError("README.md must clearly classify the repository as a public case study")
    if "python -m scripts.check" not in readme_text:
        raise ValidationError("README.md must document the canonical public validation command")


def _count_manifest_references(repo_root: Path) -> int:
    manifest = (repo_root / "public-proof/manifest/evidence-manifest.md").read_text()
    return len(_manifest_paths(manifest))


def _manifest_paths(text: str) -> list[str]:
    paths = []
    for match in MANIFEST_FILE_LINK_RE.findall(text):
        if "/" in match and not match.startswith("fixera-core"):
            paths.append(match)
    return paths


def _load_json(path: Path) -> dict:
    try:
        with path.open() as handle:
            return json.load(handle)
    except json.JSONDecodeError as exc:
        raise ValidationError(f"{path.name} is not valid JSON: {exc.msg}") from exc


def _assert_fields(payload: dict, required: set[str], label: str) -> None:
    missing = sorted(field for field in required if field not in payload)
    if missing:
        raise ValidationError(f"{label} missing required field(s): {', '.join(missing)}")


if __name__ == "__main__":
    raise SystemExit(main())
