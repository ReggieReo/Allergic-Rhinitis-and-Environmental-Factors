import unittest

from flask import json

from swagger_server.models.pm10 import Pm10  # noqa: E501
from swagger_server.test import BaseTestCase

class TestPm10(BaseTestCase):
    """Pm10 model Creating test """

    def test_valid_value(self):
        """Test case for creating Pm10 with valid input"""
        pm10_valid = 30.2
        pm10 = Pm10(pm10=pm10_valid)
        self.assertEqual(pm10.pm10, pm10_valid)

    def test_below_valid(self):
        """Test case for creating Pm10 with below valid input"""
        pm10_invalid = -4.5
        with self.assertRaises(ValueError):
            pm10 = Pm10(pm10=pm10_invalid)

    def test_nan_valid(self):
        """Test case for creating Pm10 with below valid input"""
        pm10_invalid = "Test"
        with self.assertRaises(TypeError):
            pm10 = Pm10(pm10=pm10_invalid)
