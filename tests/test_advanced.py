# -*- coding: utf-8 -*-

from .context import compareimages

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_hello(self):
        self.assertEqual(hello(), "hello world")


if __name__ == '__main__':
    unittest.main()
