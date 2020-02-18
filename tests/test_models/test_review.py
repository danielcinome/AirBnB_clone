#!/usr/bin/python3
"""Test Review"""
import unittest
import pep8
from models.review import Review
from models.user import User
from models.place import Place


class Testreview(unittest.TestCase):
    """TestReview"""
    def test_pep8_conformance_review(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors.")

    def test_review(self):
        """
        Test review
        """
        my_place = Place()
        my_user = User()
        my_review = Review()
        my_review.place_id = my_place.id
        my_review.user_id = my_user.id
        my_review.text = 'holberton'
        self.assertEqual(my_review.place_id, my_place.id)
        self.assertEqual(my_review.user_id, my_user.id)
        self.assertEqual(my_review.text, 'holberton')
