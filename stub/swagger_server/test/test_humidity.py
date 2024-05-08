import unittest

from flask import json

from swagger_server.models.humidity import Humidity  # noqa: E501
from swagger_server.test import BaseTestCase

class TestHumidity(BaseTestCase):
    """Humidity model Creating test """

    def test_valid_value(self):
        """Test case for creating Humidity with valid input"""
        hum_valid = 89
        temp = Humidity(humidity=hum_valid)
        self.assertEqual(temp.humidity, hum_valid)

    def test_below_valid(self):
        """Test case for creating Humidity with below valid input"""
        hum_invalid = -1
        with self.assertRaises(ValueError):
            temp = Humidity(humidity=hum_invalid)

    def test_above_valid(self):
        """Test case for creating Humidity with below valid input"""
        hum_invalid = 101
        with self.assertRaises(ValueError):
            temp = Humidity(humidity=hum_invalid)

    def test_nan_valid(self):
        """Test case for creating Humidity with below valid input"""
        hum_invalid = "Test"
        with self.assertRaises(TypeError):
            temp = Humidity(humidity=hum_invalid)
