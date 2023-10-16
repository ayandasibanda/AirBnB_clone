#!/usr/bin/python3
"""Module for testing the Review class"""

import unittest
import pep8
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test Review class implementation"""

    def test_doc_module(self):
        """Verify module documentation"""
        doc = Review.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_review(self):
        """Check PEP8 conformity in models/review.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_review(self):
        """Check PEP8 conformity in tests/test_models/test_review.py"""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """Verify constructor documentation"""
        doc = Review.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        """Validate the types of the attributes in the class"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(Review, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(Review.place_id, str)
            self.assertIsInstance(Review.user_id, str)
            self.assertIsInstance(Review.text, str)


if __name__ == '__main__':
    unittest.main()
