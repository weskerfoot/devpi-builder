__author__ = 'mbach'

import unittest

from brandon import requirements


class MyTestCase(unittest.TestCase):
    def test_read_requirements(self):
        expected = [
            ('progressbar', '2.0'),
            ('six', '1.3')
        ]
        self.assertListEqual(
            expected,
            requirements.read('tests/sample_simple.txt')
        )

    def test_multiple_versions(self):
        expected = [
            ('progressbar', '2.2'),
            ('progressbar', '2.1')
        ]
        self.assertListEqual(
            expected,
            requirements.read('tests/sample_multiple_versions.txt')
        )

    def test_fail_on_inexact(self):
        with self.assertRaises(ValueError):
            requirements.read('tests/sample_inexact_version.txt')

    def test_fail_on_multiple_versions_on_line(self):
        with self.assertRaises(ValueError):
            requirements.read('tests/sample_multiple_versions_on_line.txt')


if __name__ == '__main__':
    unittest.main()
