#!/usr/bin/python3
"""Test State"""
import unittest
import pep8
from models.city import City
from models.state import State


class Testcity(unittest.TestCase):
    """Teste city"""
    def test_pep8_conformance_city(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors")

    def test_city(self):
        """
            Test attributes of Class City
        """
        my_city = City()
        my_state = State()
        my_city.name = "Medellin"
        my_city.state_id = my_state.id
        self.assertEqual(my_city.name, 'Medellin')
        self.assertEqual(my_city.state_id, my_state.id)
