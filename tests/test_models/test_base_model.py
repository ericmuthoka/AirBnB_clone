#!/usr/bin/python3

"""
Unittests for BaseModel class.
"""

import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModel(unittest.TestCase):

    """
    Test cases for the BaseModel class.
    """

    def test_init(self):
        """
        Test the initialization of BaseModel attributes.
        """
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)

    def test_str(self):
        """
        Test the __str__ method of BaseModel.
        """
        instance = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(instance.id,
                                                    instance.__dict__)
        self.assertEqual(expected_str, str(instance))

    def test_save(self):
        """
        Test the save method of BaseModel.
        """
        instance = BaseModel()
        initial_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(initial_updated_at, instance.updated_at)

    def test_to_dict(self):
        """
        Test the to_dict method of BaseModel.
        """
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertEqual(instance_dict['__class__'], 'BaseModel')
        self.assertEqual(instance_dict['id'], instance.id)
        self.assertEqual(instance_dict['created_at'],
                         instance.created_at.isoformat())
        self.assertEqual(instance_dict['updated_at'],
                         instance.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
