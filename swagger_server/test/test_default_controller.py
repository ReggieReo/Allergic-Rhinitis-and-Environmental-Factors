import unittest

from flask import json

from swagger_server.models.all import All  # noqa: E501
from swagger_server.models.aqi import Aqi  # noqa: E501
from swagger_server.models.humidity import Humidity  # noqa: E501
from swagger_server.models.pm10 import Pm10  # noqa: E501
from swagger_server.models.pm25 import Pm25  # noqa: E501
from swagger_server.models.temperature import Temperature  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_controller_get_average_all(self):
        """Test case for controller_get_average_all

        Return the average temperature, humidity, aqi, pm10 and pm25 when allergy flare-ups happened.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/allergic-api/v1/average_all',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_average_aqi(self):
        """Test case for controller_get_average_aqi

        Return the average qai when allergy flare-ups happened.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/allergic-api/v1/average_aqi',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_average_humidity(self):
        """Test case for controller_get_average_humidity

        Return the average humidity when allergy flare-ups happened.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/allergic-api/v1/average_humid',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_average_pm10(self):
        """Test case for controller_get_average_pm10

        Return the average pm10 when allergy flare-ups happened.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/allergic-api/v1/average_pm10',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_average_pm25(self):
        """Test case for controller_get_average_pm25

        Return the average pm25 when allergy flare-ups happened.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/allergic-api/v1/average_pm25',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_average_temp(self):
        """Test case for controller_get_average_temp

        Return the average temperature when allergy flare-ups happened.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/allergic-api/v1/average_temp',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
