from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

import numbers
from swagger_server.models.base_model import Model
from swagger_server import util


class Humidity(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, humidity=None):  # noqa: E501
        """Humidity - a model defined in OpenAPI

        :param humidity: The humidity of this Humidity.  # noqa: E501
        :type humidity: int
        """
        if not isinstance(humidity, numbers.Number):
            raise TypeError

        if humidity > 100 or humidity < 0:
            raise ValueError

        self.openapi_types = {
            'humidity': int
        }

        self.attribute_map = {
            'humidity': 'humidity'
        }

        self._humidity = humidity

    @classmethod
    def from_dict(cls, dikt) -> 'Humidity':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Humidity of this Humidity.  # noqa: E501
        :rtype: Humidity
        """
        return util.deserialize_model(dikt, cls)

    @property
    def humidity(self) -> int:
        """Gets the humidity of this Humidity.


        :return: The humidity of this Humidity.
        :rtype: int
        """
        return self._humidity

    @humidity.setter
    def humidity(self, humidity: int):
        """Sets the humidity of this Humidity.


        :param humidity: The humidity of this Humidity.
        :type humidity: int
        """

        self._humidity = humidity
