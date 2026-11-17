# Security Policy

The conformance runner evaluates declarative JSON fixtures only; it does not load plugins or execute supplied code.

- Treat manifests and fixture files as untrusted input.
- Do not use a passing report as a security certification.
- Keep test credentials and private datasets out of public fixtures.
- Review test coverage and assumptions before relying on a result.
- Security-sensitive integration tests should run in isolated environments.

Report vulnerabilities with affected revision and a minimal sanitized reproduction.
