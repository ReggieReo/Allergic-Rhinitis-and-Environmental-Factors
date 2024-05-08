from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

import numbers
from swagger_server.models.base_model import Model
from swagger_server import util


class Pm10(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, pm10=None):  # noqa: E501
        """Pm10 - a model defined in OpenAPI

        :param pm10: The pm10 of this Pm10.  # noqa: E501
        :type pm10: int
        """
        if not isinstance(pm10, numbers.Number):
            raise TypeError

        if pm10 < 0:
            raise ValueError
        self.openapi_types = {
            'pm10': int
        }

        self.attribute_map = {
            'pm10': 'pm10'
        }

        self._pm10 = pm10

    @classmethod
    def from_dict(cls, dikt) -> 'Pm10':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Pm10 of this Pm10.  # noqa: E501
        :rtype: Pm10
        """
        return util.deserialize_model(dikt, cls)

    @property
    def pm10(self) -> int:
        """Gets the pm10 of this Pm10.


        :return: The pm10 of this Pm10.
        :rtype: int
        """
        return self._pm10

    @pm10.setter
    def pm10(self, pm10: int):
        """Sets the pm10 of this Pm10.


        :param pm10: The pm10 of this Pm10.
        :type pm10: int
        """

        self._pm10 = pm10
