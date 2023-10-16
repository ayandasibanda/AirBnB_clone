#!/usr/bin/python3
"""Module for testing the City class"""

import unittest
import pep8
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def test_doc_module(self):
        """Check if module has documentation"""
        doc = City.__doc__
        self.assertGreater(len(doc), 1)

    def test_pep8_conformance_city(self):
        """Check if models/city.py conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_city(self):
        """Check if tests/test_models/test_city.py conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        res = pep8style.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_doc_constructor(self):
        """Check if constructor has documentation"""
        doc = City.__init__.__doc__
        self.assertGreater(len(doc), 1)

    def test_class(self):
        """Validate the types of the attributes in the class"""
        with self.subTest(msg='Inheritance'):
            self.assertTrue(issubclass(City, BaseModel))

        with self.subTest(msg='Attributes'):
            self.assertIsInstance(City.name, str)
            self.assertIsInstance(City.state_id, str)


if __name__ == '__main__':
    unittest.main()
