#!/usr/bin/python3
"""Test State"""
import unittest
import pep8
from models.amenity import Amenity


class Testamenity(unittest.TestCase):
    """
        Tess amenity
    """
    def test_pep8_conformance_amenity(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors.")

    def test_amenity(self):
        """Test attributes of Class Amenity"""
        my_amenity = Amenity()
        my_amenity.name = "Wi-Fi"
        self.assertEqual(my_amenity.name, 'Wi-Fi')
