import unittest

from oif_conformance.runner import validate_manifest, run_suite


class ConformanceTests(unittest.TestCase):
    def setUp(self):
        self.manifest = {
            "id": "example.tool", "name": "Example", "resource_type": "tool",
            "publisher": {"name": "Example Publisher"}, "version": "1.0",
            "capabilities": [{"id": "example.read"}], "permissions": ["workspace.read"],
        }

    def test_valid_manifest(self):
        self.assertEqual(validate_manifest(self.manifest), [])

    def test_missing_identity(self):
        self.assertTrue(validate_manifest({}))

    def test_invalid_permissions(self):
        bad = dict(self.manifest, permissions="all")
        self.assertIn("permissions must be an array of strings", validate_manifest(bad))

    def test_fixture_counts(self):
        report = run_suite({"id": "s", "cases": [
            {"id": "pass", "assertion": "equals", "actual": 1, "expected": 1},
            {"id": "fail", "assertion": "equals", "actual": 1, "expected": 2},
        ]})
        self.assertEqual((report["total"], report["passed"], report["failed"]), (2, 1, 1))
        self.assertFalse(report["certification"])


if __name__ == "__main__":
    unittest.main()
