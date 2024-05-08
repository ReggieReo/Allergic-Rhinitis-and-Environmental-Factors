import unittest

from flask import json

from swagger_server.models.temperature import Temperature  # noqa: E501
from swagger_server.test import BaseTestCase

class TestTemperature(BaseTestCase):
    """Temperature model Creating test """

    def test_valid_value(self):
        """Test case for creating Temperature with valid input"""
        temp_valid = 30
        temp = Temperature(temperature=temp_valid)
        self.assertEqual(temp.temperature, temp_valid)

    def test_below_valid(self):
        """Test case for creating Temperature with below valid input"""
        temp_invalid = -12
        with self.assertRaises(ValueError):
            temp = Temperature(temperature=temp_invalid)

    def test_above_valid(self):
        """Test case for creating Temperature with below valid input"""
        temp_invalid = 123
        with self.assertRaises(ValueError):
            temp = Temperature(temperature=temp_invalid)

    def test_nan_valid(self):
        """Test case for creating Temperature with below valid input"""
        temp_invalid = "Test"
        with self.assertRaises(TypeError):
            temp = Temperature(temperature=temp_invalid)
