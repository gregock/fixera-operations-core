"""Run the public evidence test and validation commands."""

from __future__ import annotations

import subprocess
import sys


COMMANDS = [
    [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"],
    [sys.executable, "-m", "scripts.validate_public_evidence"],
    [sys.executable, "-m", "scripts.validate_public_docs"],
]


def main() -> int:
    for command in COMMANDS:
        completed = subprocess.run(command, check=False)
        if completed.returncode != 0:
            return completed.returncode
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
