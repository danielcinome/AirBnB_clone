#!/usr/bin/python3
""" Test Console """
from unittest.mock import patch
import unittest
import io
from io import StringIO
from console import HBNBCommand
import sys


class TestConsole(unittest.TestCase):
    def test_User(self):
        """ Tests User """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help user")

    def test_State(self):
        """ Tests State """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help state")

    def test_City(self):
        """ Tests city """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help city")

    def test_Amenity(self):
        """ Tests Amenity """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help amenity")

    def test_Place(self):
        """ Tests Place """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help place")

    def test_Review(self):
        """ Tests Review """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help review")
