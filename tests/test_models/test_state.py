#!/usr/bin/python3
"""Test State"""
import unittest
import pep8
from models.state import State


class Teststate(unittest.TestCase):
    """ Test State """
    def test_pep8_conformance_state(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors.")

    def test_state(self):
        """
        Test attributes of Class State
        """
        my_state = State()
        my_state.name = "Antioquia"
        self.assertEqual(my_state.name, 'Antioquia')
