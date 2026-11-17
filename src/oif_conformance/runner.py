"""Offline manifest and deterministic fixture conformance checks."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def validate_manifest(manifest: Any) -> list[str]:
    if not isinstance(manifest, dict):
        return ["manifest must be an object"]
    required = ("id", "name", "resource_type", "publisher", "version", "capabilities")
    errors = [f"missing required field: {key}" for key in required if key not in manifest]
    if errors:
        return errors
    for key in ("id", "name", "resource_type", "version"):
        if not isinstance(manifest[key], str) or not manifest[key].strip():
            errors.append(f"{key} must be a non-empty string")
    if not isinstance(manifest["publisher"], dict) or not isinstance(manifest["publisher"].get("name"), str):
        errors.append("publisher.name must be a string")
    if not isinstance(manifest["capabilities"], list) or not manifest["capabilities"]:
        errors.append("capabilities must be a non-empty array")
    else:
        for index, capability in enumerate(manifest["capabilities"]):
            if not isinstance(capability, dict) or not isinstance(capability.get("id"), str) or not capability["id"]:
                errors.append(f"capabilities[{index}].id must be a non-empty string")
    permissions = manifest.get("permissions", [])
    if not isinstance(permissions, list) or any(not isinstance(item, str) for item in permissions):
        errors.append("permissions must be an array of strings")
    return errors


def run_suite(suite: dict[str, Any]) -> dict[str, Any]:
    results = []
    for case in suite.get("cases", []):
        case_id = case.get("id", "<unnamed>")
        actual = case.get("actual")
        expected = case.get("expected")
        assertion = case.get("assertion", "equals")
        if assertion == "equals":
            passed = actual == expected
        elif assertion == "contains_keys":
            passed = isinstance(actual, dict) and all(key in actual for key in expected)
        else:
            passed = False
        results.append({"id": case_id, "passed": bool(passed), "assertion": assertion})
    return {
        "suite_id": suite.get("id", "unnamed-suite"),
        "total": len(results),
        "passed": sum(1 for item in results if item["passed"]),
        "failed": sum(1 for item in results if not item["passed"]),
        "results": results,
        "certification": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run an offline OIF conformance fixture suite.")
    sub = parser.add_subparsers(dest="command", required=True)
    run = sub.add_parser("run")
    run.add_argument("suite", type=Path)
    args = parser.parse_args()
    suite = json.loads(args.suite.read_text(encoding="utf-8"))
    report = run_suite(suite)
    print(json.dumps(report, indent=2, sort_keys=True))
    return 1 if report["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
