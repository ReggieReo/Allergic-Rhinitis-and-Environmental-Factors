import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from swagger_server.models.all import All  # noqa: E501
from swagger_server.models.aqi import Aqi  # noqa: E501
from swagger_server.models.humidity import Humidity  # noqa: E501
from swagger_server.models.pm10 import Pm10  # noqa: E501
from swagger_server.models.pm25 import Pm25  # noqa: E501
from swagger_server.models.temperature import Temperature  # noqa: E501
from swagger_server import util, database_util

pool = database_util.DataBase()

def controller_get_average_all():  # noqa: E501
    """Return the average temperature, humidity, aqi, pm10 and pm25 when allergy flare-ups happened.

     # noqa: E501

    :rtype: Union[All, Tuple[All, int], Tuple[All, int, Dict[str, str]]
    """
    result = pool.get_average_all()
    return "temp"


def controller_get_average_aqi():  # noqa: E501
    """Return the average qai when allergy flare-ups happened.

     # noqa: E501


    :rtype: Union[Aqi, Tuple[Aqi, int], Tuple[Aqi, int, Dict[str, str]]
    """
    result = Aqi(pool.get_average_aqi())
    return result


def controller_get_average_humidity():  # noqa: E501
    """Return the average humidity when allergy flare-ups happened.

     # noqa: E501


    :rtype: Union[Humidity, Tuple[Humidity, int], Tuple[Humidity, int, Dict[str, str]]
    """
    result = Humidity(pool.get_average_hum())
    return result


def controller_get_average_pm10():  # noqa: E501
    """Return the average pm10 when allergy flare-ups happened.

     # noqa: E501


    :rtype: Union[Pm10, Tuple[Pm10, int], Tuple[Pm10, int, Dict[str, str]]
    """
    result = Pm10(pool.get_average_pm10())
    return result


def controller_get_average_pm25():  # noqa: E501
    """Return the average pm25 when allergy flare-ups happened.

     # noqa: E501


    :rtype: Union[Pm25, Tuple[Pm25, int], Tuple[Pm25, int, Dict[str, str]]
    """
    result = Pm25(pool.get_average_pm25())
    return result


def controller_get_average_temp():  # noqa: E501
    """Return the average temperature when allergy flare-ups happened.

     # noqa: E501


    :rtype: Union[Temperature, Tuple[Temperature, int], Tuple[Temperature, int, Dict[str, str]]
    """
    result = Temperature(pool.get_average_temp())
    return result
