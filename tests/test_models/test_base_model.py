#!/usr/bin/python3
"""Test Base Model"""
import unittest
import pep8
from datetime import datetime
import uuid
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review


class Testpep8(unittest.TestCase):

    def test_pep8_conformance_base_model(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class Testbasemodel(unittest.TestCase):

    def test_creation_from_dictionary_basic(self):
        """ This function proves in a basic way that when instantiating\
            by passing a dictionary, it works correctly """
        date = datetime.now()
        dic = {"id": "7734cf23-6c89-4662-8483-284727324c77", "created_at":
               "2020-02-17T16:32:39.023915", "updated_at":
               "2020-02-17T16:32:39.023940", "__class__": "BaseModel"}
        my_base = BaseModel(**dic)
        self.assertEqual(my_base.__class__.__name__, "BaseModel")
        self.assertEqual(my_base.id, "7734cf23-6c89-4662-8483-284727324c77")
        self.assertEqual(type(my_base.created_at), type(date))
        self.assertEqual(type(my_base.updated_at), type(date))

    def test_creation_from_dictionary_advanced(self):
        """ This function proves that when passing a dictionary with\
            extra attributes, these are added correctly """
        date = datetime.now()
        dic = {"id": "7734cf23-6c89-4662-8483-284727324c77", "created_at":
               "2020-02-17T16:32:39.023915", "updated_at":
               "2020-02-17T16:32:39.023940", "__class__": "BaseModel",
               "name": "Andrea", "last_name": "Méndez"}
        my_base = BaseModel(**dic)
        self.assertEqual(my_base.__class__.__name__, "BaseModel")
        self.assertEqual(my_base.id, "7734cf23-6c89-4662-8483-284727324c77")
        self.assertEqual(type(my_base.created_at), type(date))
        self.assertEqual(type(my_base.updated_at), type(date))
        self.assertEqual(my_base.name, "Andrea")
        self.assertEqual(my_base.last_name, "Méndez")

    def test_creation_from_dictionary_advancedx2(self):
        """ This function proves that when passing a dictionary with\
            extra attributes of numeric type, these are added correctly
            and their types correspond """
        date = datetime.now()
        dic = {"id": "7734cf23-6c89-4662-8483-284727324c77", "created_at":
               "2020-02-17T16:32:39.023915", "updated_at":
               "2020-02-17T16:32:39.023940", "__class__": "BaseModel", "name":
               "Andrea", "last_name": "Méndez", "age": 20, "height": 1.68}
        my_base = BaseModel(**dic)
        self.assertEqual(my_base.__class__.__name__, "BaseModel")
        self.assertEqual(my_base.id, "7734cf23-6c89-4662-8483-284727324c77")
        self.assertEqual(type(my_base.created_at), type(date))
        self.assertEqual(type(my_base.updated_at), type(date))
        self.assertEqual(my_base.name, "Andrea")
        self.assertEqual(my_base.last_name, "Méndez")
        self.assertEqual(my_base.age, 20)
        self.assertEqual(my_base.height, 1.68)
        self.assertEqual(type(my_base.age), int)
        self.assertEqual(type(my_base.height), float)

    def test_creation_from_dictionary_advancedx3(self):
        """ This function proves that when passing a dictionary with\
            extra attributes and with spaces in those of type string,\
            these are added correctly """
        date = datetime.now()
        dic = {"id": "7734cf23-6c89-4662-8483-284727324c77", "created_at":
               "2020-02-17T16:32:39.023915", "updated_at":
               "2020-02-17T16:32:39.023940", "__class__": "BaseModel", "name":
               "Andrea", "last_name": "Méndez Mesias"}
        my_base = BaseModel(**dic)
        self.assertEqual(my_base.__class__.__name__, "BaseModel")
        self.assertEqual(my_base.id, "7734cf23-6c89-4662-8483-284727324c77")
        self.assertEqual(type(my_base.created_at), type(date))
        self.assertEqual(type(my_base.updated_at), type(date))
        self.assertEqual(my_base.name, "Andrea")
        self.assertEqual(my_base.last_name, "Méndez Mesias")
        self.assertEqual(type(my_base.last_name), str)

    def test_isinstance(self):
        """"Test if is an instance of the class"""
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_init(self):
        """Test __init__
        """
        base = BaseModel()
        self.assertTrue(hasattr(base, "id"))
        self.assertTrue(hasattr(base, "created_at"))
        self.assertTrue(hasattr(base, "updated_at"))

    def test_id(self):
        """Test id
        """
        base0 = BaseModel()
        base1 = BaseModel()
        self.assertEqual(uuid.UUID(base0.id).version, 4)
        self.assertFalse(base0.id == base1.id)

    def test_to_dict(self):
        """Tests the to_dict function."""
        obj = BaseModel()
        new_dict = obj.__dict__.copy()
        new_dict["__class__"] = obj.__class__.__name__
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        comparing = obj.to_dict()
        self.assertDictEqual(new_dict, comparing)

    def test_save_BaseModel(self):
        """test if the save method works"""
        obj = BaseModel()
        obj.save()
        self.assertNotEqual(obj.created_at, obj.updated_at)

    def test_checking_for_docstring_BaseModel(self):
        """checking for docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_method_BaseModel(self):
        """checking if Basemodel have methods"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_base_model_updated_at_is_datetime(self):
        """Datetime test.
        This test is designed to check if the date and time in which a
        class is updated are correctly assigned.
        """
        bm = BaseModel()
        self.assertIsInstance(bm.updated_at, datetime)

    def test_base_model_created_at_is_datetime(self):
        """Datetime test.
        This test is designed to check if the date and time in which a
        class was created are correctly assigned.
        """
        bm = BaseModel()
        self.assertIsInstance(bm.created_at, datetime)

    def test_base_model_different_uuid(self):
        """...
        ...
        ...
        """
        bm_one = BaseModel()
        bm_two = BaseModel()
        conv_uuid_one = uuid.UUID(bm_one.id)
        conv_uuid_two = uuid.UUID(bm_two.id)
        self.assertNotEqual(conv_uuid_one, conv_uuid_two)

    def test_base_model_id_is_string(self):
        """UUID format testing.
        This test is designed to check if any generated UUID
        is correctly generated and has the propper format.
        """
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)

    def test_base_model_uuid_good_format(self):
        """...
        ...
        ...
        """
        bm = BaseModel()
        self.assertIsInstance(uuid.UUID(bm.id), uuid.UUID)

    def test_base_model_uuid_wrong_format(self):
        """...
        ...
        ...
        """
        bm = BaseModel()
        bm.id = 'Monty Python'
        warn = 'badly formed hexadecimal UUID string'
        with self.assertRaises(ValueError) as msg:
            uuid.UUID(bm.id)
        self.assertEqual(warn, str(msg.exception))

    def test_base_model_uuid_version(self):
        """...
        ...
        ...
        """
        bm = BaseModel()
        conv_uuid = uuid.UUID(bm.id)
        self.assertEqual(conv_uuid.version, 4)
