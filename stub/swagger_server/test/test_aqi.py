import unittest

from flask import json

from swagger_server.models.aqi import Aqi  # noqa: E501
from swagger_server.test import BaseTestCase

class TestAqi(BaseTestCase):
    """Aqi model Creating test """

    def test_valid_value(self):
        """Test case for creating Aqi with valid input"""
        aqi_valid = 101
        aqi = Aqi(aqi=aqi_valid)
        self.assertEqual(aqi.aqi, aqi_valid)

    def test_below_valid(self):
        """Test case for creating Aqi with below valid input"""
        aqi_invalid = -5
        with self.assertRaises(ValueError):
            aqi = Aqi(aqi=aqi_invalid)

    def test_above_valid(self):
        """Test case for creating Aqi with below valid input"""
        aqi_invalid = 696
        with self.assertRaises(ValueError):
            aqi = Aqi(aqi=aqi_invalid)

    def test_nan_valid(self):
        """Test case for creating Aqi with below valid input"""
        aqi_invalid = "Test"
        with self.assertRaises(TypeError):
            aqi = Aqi(aqi=aqi_invalid)
