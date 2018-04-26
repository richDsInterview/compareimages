# -*- coding: utf-8 -*-

from .context import compareimages

import unittest

class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_hello(self):
        self.assertEqual(hello(), "hello")

    def test_compare_images_exact(self):
        self.assertAlmostEquals(
            compareimages.compare_images_exact(
                "./Data_Science_Images/Test/test_image5.jpg",
                "./Data_Science_Images/Training/training_image4.jpg")
            , 1.0)
    def test_compare_images_scaled(self):
        self.assertAlmostEquals(
            compareimages.compare_images_scaled(
                "./Data_Science_Images/Test/test_image4.jpg",
                "./Data_Science_Images/Training/training_image3.jpg")
            , 1.0)

    def test_compare_images_phash(self):
        self.assertAlmostEquals(
            compareimages.compare_images_scaled(
                "./Data_Science_Images/Test/test_image4.jpg",
                "./Data_Science_Images/Training/training_image3.jpg")
            , 1.0)
if __name__ == '__main__':
    unittest.main()
