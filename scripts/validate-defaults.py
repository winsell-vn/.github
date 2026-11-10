#!/usr/bin/env python3
"""Validate the organization-wide default files in this repository.

GitHub silently ignores a malformed issue form, discussion form or starter
workflow. This script fails the build instead, so a broken default never
reaches every repository in the organization.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover - dependency is installed in CI
    print("PyYAML is required: pip install pyyaml", file=sys.stderr)
    raise SystemExit(1)

ROOT = Path(__file__).resolve().parent.parent
ISSUE_TEMPLATE_DIR = ROOT / ".github" / "ISSUE_TEMPLATE"
DISCUSSION_TEMPLATE_DIR = ROOT / ".github" / "DISCUSSION_TEMPLATE"
TEMPLATE_DIR = ROOT / "workflow-templates"

failures: list[str] = []


def check_forms(directory: Path, skip: set[str]) -> None:
    """Every form file must be a mapping with a body."""
    if not directory.is_dir():
        return
    for path in sorted(directory.glob("*.yml")):
        if path.name in skip:
            print(f"skip  {path.relative_to(ROOT)} (not a form)")
            continue
        try:
            doc = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as err:
            failures.append(f"{path.relative_to(ROOT)}: invalid YAML: {err}")
            continue
        if not isinstance(doc, dict):
            failures.append(f"{path.relative_to(ROOT)}: expected a mapping")
            continue
        if "body" not in doc:
            failures.append(f'{path.relative_to(ROOT)}: missing required key "body"')
            continue
        print(f"ok    {path.relative_to(ROOT)}")


def check_workflow_templates() -> None:
    """Every starter workflow needs metadata and must parse as YAML."""
    if not TEMPLATE_DIR.is_dir():
        return
    for template in sorted(TEMPLATE_DIR.glob("*.yml")):
        rel = template.relative_to(ROOT)
        try:
            yaml.safe_load(template.read_text(encoding="utf-8"))
        except yaml.YAMLError as err:
            failures.append(f"{rel}: invalid YAML: {err}")
            continue
        print(f"ok    {rel}")

        meta = template.parent / (template.stem + ".properties.json")
        if not meta.is_file():
            failures.append(f"{rel}: missing {meta.name}")
            continue
        try:
            doc = json.loads(meta.read_text(encoding="utf-8"))
        except json.JSONDecodeError as err:
            failures.append(f"{meta.relative_to(ROOT)}: invalid JSON: {err}")
            continue
        missing = [key for key in ("name", "description") if not doc.get(key)]
        if missing:
            failures.append(
                f"{meta.relative_to(ROOT)}: missing key(s) {', '.join(missing)}"
            )
            continue
        print(f"ok    {meta.relative_to(ROOT)}")


def main() -> int:
    check_forms(ISSUE_TEMPLATE_DIR, skip={"config.yml"})
    check_forms(DISCUSSION_TEMPLATE_DIR, skip=set())
    check_workflow_templates()

    if failures:
        print("\nvalidation failed:", file=sys.stderr)
        for failure in failures:
            print(f"  - {failure}", file=sys.stderr)
        return 1
    print("\nall organization defaults are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
