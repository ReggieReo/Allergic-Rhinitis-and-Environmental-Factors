import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from swagger_server.models.all import All  # noqa: E501
from swagger_server.models.all_with_date_and_allergic import AllWithDateAndAllergic  # noqa: E501
from swagger_server.models.aqi import Aqi  # noqa: E501
from swagger_server.models.humidity import Humidity  # noqa: E501
from swagger_server.models.pm10 import Pm10  # noqa: E501
from swagger_server.models.pm25 import Pm25  # noqa: E501
from swagger_server.models.temperature import Temperature  # noqa: E501
from swagger_server import util


def controller_get_average_all():  # noqa: E501
    """Return the average temperature, humidity, aqi, pm10 and pm25 when allergic rhinitis happened.

     # noqa: E501


    :rtype: Union[All, Tuple[All, int], Tuple[All, int, Dict[str, str]]
    """
    return 'do some magic!'


def controller_get_average_aqi():  # noqa: E501
    """Return the average qai when allergic rhinitis happened.

     # noqa: E501


    :rtype: Union[Aqi, Tuple[Aqi, int], Tuple[Aqi, int, Dict[str, str]]
    """
    return 'do some magic!'


def controller_get_average_given_date(date):  # noqa: E501
    """Given date in the parameter return average eviropment factor along with does allergic rhinitis happen on that day.

     # noqa: E501

    :param _date: 
    :type _date: str

    :rtype: Union[AllWithDateAndAllergic, Tuple[AllWithDateAndAllergic, int], Tuple[AllWithDateAndAllergic, int, Dict[str, str]]
    """
    return 'do some magic!'


def controller_get_average_humidity():  # noqa: E501
    """Return the average humidity when allergic rhinitis happened.

     # noqa: E501


    :rtype: Union[Humidity, Tuple[Humidity, int], Tuple[Humidity, int, Dict[str, str]]
    """
    return 'do some magic!'


def controller_get_average_pm10():  # noqa: E501
    """Return the average pm10 when allergic rhinitis happened.

     # noqa: E501


    :rtype: Union[Pm10, Tuple[Pm10, int], Tuple[Pm10, int, Dict[str, str]]
    """
    return 'do some magic!'


def controller_get_average_pm25():  # noqa: E501
    """Return the average pm25 when allergic rhinitis happened.

     # noqa: E501


    :rtype: Union[Pm25, Tuple[Pm25, int], Tuple[Pm25, int, Dict[str, str]]
    """
    return 'do some magic!'


def controller_get_average_temp():  # noqa: E501
    """Return the average temperature when allergic rhinitis happened.

     # noqa: E501


    :rtype: Union[Temperature, Tuple[Temperature, int], Tuple[Temperature, int, Dict[str, str]]
    """
    return 'do some magic!'


def controller_get_max_all():  # noqa: E501
    """Return the maximum temperature, humidity, aqi, pm10 and pm25 when allergic rhinitis happened.

     # noqa: E501


    :rtype: Union[All, Tuple[All, int], Tuple[All, int, Dict[str, str]]
    """
    return 'do some magic!'


def controller_get_max_aqi():  # noqa: E501
    """Return the maximum qai when allergic rhinitis happened.

     # noqa: E501


    :rtype: Union[Aqi, Tuple[Aqi, int], Tuple[Aqi, int, Dict[str, str]]
    """
    return 'do some magic!'


def controller_get_max_given_date(date):  # noqa: E501
    """Given date in the parameter return maximum eviropment factor along with does allergic rhinitis happen on that day.

     # noqa: E501

    :param _date: 
    :type _date: str

    :rtype: Union[AllWithDateAndAllergic, Tuple[AllWithDateAndAllergic, int], Tuple[AllWithDateAndAllergic, int, Dict[str, str]]
    """
    return 'do some magic!'


def controller_get_max_humidity():  # noqa: E501
    """Return the maximum humidity when allergic rhinitis happened.

     # noqa: E501


    :rtype: Union[Humidity, Tuple[Humidity, int], Tuple[Humidity, int, Dict[str, str]]
    """
    return 'do some magic!'


def controller_get_max_pm10():  # noqa: E501
    """Return the maximum pm10 when allergic rhinitis happened.

     # noqa: E501


    :rtype: Union[Pm10, Tuple[Pm10, int], Tuple[Pm10, int, Dict[str, str]]
    """
    return 'do some magic!'


def controller_get_max_pm25():  # noqa: E501
    """Return the maximum pm25 when allergic rhinitis happened.

     # noqa: E501


    :rtype: Union[Pm25, Tuple[Pm25, int], Tuple[Pm25, int, Dict[str, str]]
    """
    return 'do some magic!'


def controller_get_max_temp():  # noqa: E501
    """Return the maximum temperature when allergic rhinitis happened.

     # noqa: E501


    :rtype: Union[Temperature, Tuple[Temperature, int], Tuple[Temperature, int, Dict[str, str]]
    """
    return 'do some magic!'


def controller_get_min_all():  # noqa: E501
    """Return the minimum temperature, humidity, aqi, pm10 and pm25 when allergic rhinitis happened.

     # noqa: E501


    :rtype: Union[All, Tuple[All, int], Tuple[All, int, Dict[str, str]]
    """
    return 'do some magic!'


def controller_get_min_aqi():  # noqa: E501
    """Return the minimum qai when allergic rhinitis happened.

     # noqa: E501


    :rtype: Union[Aqi, Tuple[Aqi, int], Tuple[Aqi, int, Dict[str, str]]
    """
    return 'do some magic!'


def controller_get_min_given_date(date):  # noqa: E501
    """Given date in the parameter return minimum eviropment factor along with does allergic rhinitis happen on that day.

     # noqa: E501

    :param _date: 
    :type _date: str

    :rtype: Union[AllWithDateAndAllergic, Tuple[AllWithDateAndAllergic, int], Tuple[AllWithDateAndAllergic, int, Dict[str, str]]
    """
    return 'do some magic!'


def controller_get_min_humidity():  # noqa: E501
    """Return the minimum humidity when allergic rhinitis happened.

     # noqa: E501


    :rtype: Union[Humidity, Tuple[Humidity, int], Tuple[Humidity, int, Dict[str, str]]
    """
    return 'do some magic!'


def controller_get_min_pm10():  # noqa: E501
    """Return the minimum pm10 when allergic rhinitis happened.

     # noqa: E501


    :rtype: Union[Pm10, Tuple[Pm10, int], Tuple[Pm10, int, Dict[str, str]]
    """
    return 'do some magic!'


def controller_get_min_pm25():  # noqa: E501
    """Return the minimum pm25 when allergic rhinitis happened.

     # noqa: E501


    :rtype: Union[Pm25, Tuple[Pm25, int], Tuple[Pm25, int, Dict[str, str]]
    """
    return 'do some magic!'


def controller_get_min_temp():  # noqa: E501
    """Return the minimum temperature when allergic rhinitis happened.

     # noqa: E501


    :rtype: Union[Temperature, Tuple[Temperature, int], Tuple[Temperature, int, Dict[str, str]]
    """
    return 'do some magic!'
