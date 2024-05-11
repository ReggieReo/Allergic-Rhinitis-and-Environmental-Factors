import unittest

from flask import json

from swagger_server.models.all import All  # noqa: E501
from swagger_server.models.all_with_date_and_allergic import AllWithDateAndAllergic  # noqa: E501
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

        Return the average temperature, humidity, aqi, pm10 and pm25 when allergic rhinitis happened.
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

        Return the average qai when allergic rhinitis happened.
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

    def test_controller_get_average_given_date(self):
        """Test case for controller_get_average_given_date

        Given date in the parameter return average eviropment factor along with does allergic rhinitis happen on that day.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/allergic-api/v1/average_given_date/{_date}'.format(_date='2024-05-24'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_average_humidity(self):
        """Test case for controller_get_average_humidity

        Return the average humidity when allergic rhinitis happened.
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

        Return the average pm10 when allergic rhinitis happened.
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

        Return the average pm25 when allergic rhinitis happened.
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

        Return the average temperature when allergic rhinitis happened.
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

    def test_controller_get_max_all(self):
        """Test case for controller_get_max_all

        Return the maximum temperature, humidity, aqi, pm10 and pm25 when allergic rhinitis happened.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/allergic-api/v1/max_all',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_max_aqi(self):
        """Test case for controller_get_max_aqi

        Return the maximum qai when allergic rhinitis happened.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/allergic-api/v1/max_aqi',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_max_given_date(self):
        """Test case for controller_get_max_given_date

        Given date in the parameter return maximum eviropment factor along with does allergic rhinitis happen on that day.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/allergic-api/v1/max_given_date/{_date}'.format(_date='_date_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_max_humidity(self):
        """Test case for controller_get_max_humidity

        Return the maximum humidity when allergic rhinitis happened.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/allergic-api/v1/max_humid',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_max_pm10(self):
        """Test case for controller_get_max_pm10

        Return the maximum pm10 when allergic rhinitis happened.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/allergic-api/v1/max_pm10',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_max_pm25(self):
        """Test case for controller_get_max_pm25

        Return the maximum pm25 when allergic rhinitis happened.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/allergic-api/v1/max_pm25',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_max_temp(self):
        """Test case for controller_get_max_temp

        Return the maximum temperature when allergic rhinitis happened.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/allergic-api/v1/max_temp',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_min_all(self):
        """Test case for controller_get_min_all

        Return the minimum temperature, humidity, aqi, pm10 and pm25 when allergic rhinitis happened.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/allergic-api/v1/min_all',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_min_aqi(self):
        """Test case for controller_get_min_aqi

        Return the minimum qai when allergic rhinitis happened.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/allergic-api/v1/min_aqi',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_min_given_date(self):
        """Test case for controller_get_min_given_date

        Given date in the parameter return minimum eviropment factor along with does allergic rhinitis happen on that day.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/allergic-api/v1/min_given_date/{_date}'.format(_date='_date_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_min_humidity(self):
        """Test case for controller_get_min_humidity

        Return the minimum humidity when allergic rhinitis happened.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/allergic-api/v1/min_humid',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_min_pm10(self):
        """Test case for controller_get_min_pm10

        Return the minimum pm10 when allergic rhinitis happened.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/allergic-api/v1/min_pm10',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_min_pm25(self):
        """Test case for controller_get_min_pm25

        Return the minimum pm25 when allergic rhinitis happened.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/allergic-api/v1/min_pm25',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_controller_get_min_temp(self):
        """Test case for controller_get_min_temp

        Return the minimum temperature when allergic rhinitis happened.
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/allergic-api/v1/min_temp',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
