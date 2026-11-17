# OIF Conformance Lab

**Offline checks for Open Intelligence resource manifests and deterministic behavior fixtures.**

The Conformance Lab provides a small validation runner for resource manifests and declarative test cases. It checks required identity and capability fields, validates declared permission boundaries, and evaluates simple expected-output fixtures. It does not certify an implementation, execute arbitrary plugin code, or establish security from a passing test suite.

## Implemented

- Required-field checks for OI resource manifests.
- Validation of capability identifiers and declared permission arrays.
- Deterministic fixture runner for equality and required-key assertions.
- Machine-readable JSON report with pass/fail counts.
- Tests for malformed manifests, permission declarations, and fixture outcomes.

## Quick start

```bash
python -m pip install -e .
python -m unittest discover -s tests -v
oif-conformance run examples/suite.json
```

No external service or third-party runtime dependency is required.

## Conformance versus certification

A passing local suite means only that the tested inputs satisfied the implemented assertions. It does not prove correctness, safety, interoperability with every peer, or resistance to malicious inputs. Reports include the suite identifier and individual case results so evidence can be reviewed.

## Scope

This repository owns offline conformance checks and reproducible test fixtures. Shared interface definitions belong in [Open-Intelligence-Fabric](https://github.com/HuffmanMainNode/Open-Intelligence-Fabric); AI-specific security controls belong in [OIF-AI-Security](https://github.com/HuffmanMainNode/OIF-AI-Security).
