import unittest

from flask import json

from swagger_server.models.pm25 import Pm25  # noqa: E501
from swagger_server.test import BaseTestCase

class TestPm25(BaseTestCase):
    """Pm25 model Creating test """

    def test_valid_value(self):
        """Test case for creating Pm25 with valid input"""
        pm25_valid = 20.2
        pm25 = Pm25(pm25=pm25_valid)
        self.assertEqual(pm25.pm25, pm25_valid)

    def test_below_valid(self):
        """Test case for creating Pm25 with below valid input"""
        pm25_invalid = -1.1
        with self.assertRaises(ValueError):
            pm25 = Pm25(pm25=pm25_invalid)

    def test_nan_valid(self):
        """Test case for creating Pm25 with below valid input"""
        pm25_invalid = "Test"
        with self.assertRaises(TypeError):
            pm25 = Pm25(pm25=pm25_invalid)
