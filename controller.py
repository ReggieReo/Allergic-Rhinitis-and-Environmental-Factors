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
from swagger_server.models.all_with_date_and_allergic import AllWithDateAndAllergic # noqa: E501
from swagger_server import util
import database_util

pool = database_util.DataBase()

def get_average_all():  # noqa: E501
    """Return the average temperature, humidity, aqi, pm10 and pm25 when allergy flare-ups happened.

     # noqa: E501

    :rtype: Union[All, Tuple[All, int], Tuple[All, int, Dict[str, str]]
    """
    result = pool.get_average_all()
    aqi, pm10, pm25, temp, hum = result
    result = All(temperature=temp, humidity=hum, pm25=pm25, pm10=pm10, aqi=aqi)
    return result


def get_average_aqi():  # noqa: E501
    """Return the average qai when allergy flare-ups happened.

     # noqa: E501


    :rtype: Union[Aqi, Tuple[Aqi, int], Tuple[Aqi, int, Dict[str, str]]
    """
    result = Aqi(pool.get_average_aqi())
    return result


def get_average_humidity():  # noqa: E501
    """Return the average humidity when allergy flare-ups happened.

     # noqa: E501


    :rtype: Union[Humidity, Tuple[Humidity, int], Tuple[Humidity, int, Dict[str, str]]
    """
    result = Humidity(pool.get_average_hum())
    return result


def get_average_pm10():  # noqa: E501
    """Return the average pm10 when allergy flare-ups happened.

     # noqa: E501


    :rtype: Union[Pm10, Tuple[Pm10, int], Tuple[Pm10, int, Dict[str, str]]
    """
    result = Pm10(pool.get_average_pm10())
    return result


def get_average_pm25():  # noqa: E501
    """Return the average pm25 when allergy flare-ups happened.

     # noqa: E501


    :rtype: Union[Pm25, Tuple[Pm25, int], Tuple[Pm25, int, Dict[str, str]]
    """
    result = Pm25(pool.get_average_pm25())
    return result


def get_average_temp():  # noqa: E501
    """Return the average temperature when allergy flare-ups happened.

     # noqa: E501


    :rtype: Union[Temperature, Tuple[Temperature, int], Tuple[Temperature, int, Dict[str, str]]
    """
    result = Temperature(pool.get_average_temp())
    return result

# minimum
def get_min_all():  # noqa: E501
    """Return the minimum temperature, humidity, aqi, pm10 and pm25 when allergy flare-ups happened.

     # noqa: E501

    :rtype: Union[All, Tuple[All, int], Tuple[All, int, Dict[str, str]]
    """
    result = pool.get_min_all()
    aqi, pm10, pm25, temp, hum = result
    result = All(temperature=temp, humidity=hum, pm25=pm25, pm10=pm10, aqi=aqi)
    return result


def get_min_aqi():  # noqa: E501
    """Return the minimum aqi when allergy flare-ups happened.

     # noqa: E501


    :rtype: Union[Aqi, Tuple[Aqi, int], Tuple[Aqi, int, Dict[str, str]]
    """
    result = Aqi(pool.get_min_aqi())
    return result


def get_min_humidity():  # noqa: E501
    """Return the minimum humidity when allergy flare-ups happened.

     # noqa: E501


    :rtype: Union[Humidity, Tuple[Humidity, int], Tuple[Humidity, int, Dict[str, str]]
    """
    result = Humidity(pool.get_min_hum())
    return result


def get_min_pm10():  # noqa: E501
    """Return the minimum pm10 when allergy flare-ups happened.

     # noqa: E501


    :rtype: Union[Pm10, Tuple[Pm10, int], Tuple[Pm10, int, Dict[str, str]]
    """
    result = Pm10(pool.get_min_pm10())
    return result


def get_min_pm25():  # noqa: E501
    """Return the minimum pm25 when allergy flare-ups happened.

     # noqa: E501


    :rtype: Union[Pm25, Tuple[Pm25, int], Tuple[Pm25, int, Dict[str, str]]
    """
    result = Pm25(pool.get_min_pm25())
    return result


def get_min_temp():  # noqa: E501
    """Return the minimum temperature when allergy flare-ups happened.

     # noqa: E501


    :rtype: Union[Temperature, Tuple[Temperature, int], Tuple[Temperature, int, Dict[str, str]]
    """
    result = Temperature(pool.get_min_temp())
    return result

# maximum 
def get_max_all():  # noqa: E501
    """Return the maximum temperature, humidity, aqi, pm10 and pm25 when allergy flare-ups happened.

     # noqa: E501

    :rtype: Union[All, Tuple[All, int], Tuple[All, int, Dict[str, str]]
    """
    result = pool.get_max_all()
    aqi, pm10, pm25, temp, hum = result
    result = All(temperature=temp, humidity=hum, pm25=pm25, pm10=pm10, aqi=aqi)
    return result


def get_max_aqi():  # noqa: E501
    """Return the maximum aqi when allergy flare-ups happened.

     # noqa: E501


    :rtype: Union[Aqi, Tuple[Aqi, int], Tuple[Aqi, int, Dict[str, str]]
    """
    result = Aqi(pool.get_max_aqi())
    return result


def get_max_humidity():  # noqa: E501
    """Return the maximum humidity when allergy flare-ups happened.

     # noqa: E501


    :rtype: Union[Humidity, Tuple[Humidity, int], Tuple[Humidity, int, Dict[str, str]]
    """
    result = Humidity(pool.get_max_hum())
    return result


def get_max_pm10():  # noqa: E501
    """Return the maximum pm10 when allergy flare-ups happened.

     # noqa: E501


    :rtype: Union[Pm10, Tuple[Pm10, int], Tuple[Pm10, int, Dict[str, str]]
    """
    result = Pm10(pool.get_max_pm10())
    return result


def get_max_pm25():  # noqa: E501
    """Return the maximum pm25 when allergy flare-ups happened.

     # noqa: E501


    :rtype: Union[Pm25, Tuple[Pm25, int], Tuple[Pm25, int, Dict[str, str]]
    """
    result = Pm25(pool.get_max_pm25())
    return result


def get_max_temp():  # noqa: E501
    """Return the maximum temperature when allergy flare-ups happened.

     # noqa: E501


    :rtype: Union[Temperature, Tuple[Temperature, int], Tuple[Temperature, int, Dict[str, str]]
    """
    result = Temperature(pool.get_max_temp())
    return result

# date 
def get_average_given_date(date):  # noqa: E501
    """Given date in the parameter return average eviropment factor along with does allergic rhinitis happen on that day.

     # noqa: E501

    :param _date: 
    :type _date: str

    :rtype: Union[AllWithDateAndAllergic, Tuple[AllWithDateAndAllergic, int], Tuple[AllWithDateAndAllergic, int, Dict[str, str]]
    """
    result = pool.get_average_all_with_date(date)
    if not result:
        return "Does not have data on that date"
    aqi, pm10, pm25, temp, humid, date, flare_up = result
    if flare_up > 0:
        flare_up = True
    else:
        flare_up = False
    reponse = AllWithDateAndAllergic(temperature=temp, humidity=humid, pm25=pm25, pm10=pm10, aqi=aqi, allergic_rhinitis=flare_up, _date=date)
    return reponse

def get_min_given_date(date):  # noqa: E501
    """Given date in the parameter return minimum eviropment factor along with does allergic rhinitis happen on that day.

     # noqa: E501

    :param _date: 
    :type _date: str

    :rtype: Union[AllWithDateAndAllergic, Tuple[AllWithDateAndAllergic, int], Tuple[AllWithDateAndAllergic, int, Dict[str, str]]
    """
    result = pool.get_min_all_with_date(date)
    if not result:
        return "Does not have data on that date"
    aqi, pm10, pm25, temp, humid, date, flare_up = result
    if flare_up > 0:
        flare_up = True
    else:
        flare_up = False
    reponse = AllWithDateAndAllergic(temperature=temp, humidity=humid, pm25=pm25, pm10=pm10, aqi=aqi, allergic_rhinitis=flare_up, _date=date)
    return reponse

def get_max_given_date(date):  # noqa: E501
    """Given date in the parameter return maximum eviropment factor along with does allergic rhinitis happen on that day.

     # noqa: E501

    :param _date: 
    :type _date: str

    :rtype: Union[AllWithDateAndAllergic, Tuple[AllWithDateAndAllergic, int], Tuple[AllWithDateAndAllergic, int, Dict[str, str]]
    """
    result = pool.get_max_all_with_date(date)
    if not result:
        return "Does not have data on that date"
    aqi, pm10, pm25, temp, humid, date, flare_up = result
    if flare_up > 0:
        flare_up = True
    else:
        flare_up = False
    reponse = AllWithDateAndAllergic(temperature=temp, humidity=humid, pm25=pm25, pm10=pm10, aqi=aqi, allergic_rhinitis=flare_up, _date=date)
    return reponse
