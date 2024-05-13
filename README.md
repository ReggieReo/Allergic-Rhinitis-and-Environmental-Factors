# Allergic Rhinitis and Environmental Factors
Github repository:<br>
[API server](https://github.com/ReggieReo/Allergic-Rhinitis-and-Environmental-Factors)<br>
[Visualization](https://github.com/ReggieReo/Allergic-Visualisation)

## Members
| Student ID | Name|
| -------- | ------- |
| 6510545764| Setthapon Thadisakun|
| 6510545420 |Tantikon Phasanphaengsi|

## Overview
Allergic Rhinitis and Environmetal Factors investigates how environmental factors influence allergy symptoms. We focus collecting on environmental factors such as data on dust levels, temperature, and humidity, as these elements could affect allergic rhinitis. We will also survey individuals with allergic rhinitis to determine whether they experience symptoms in the morning.<br>
All data were collected between 15-04-2024 to 10-05-2024 <br>
This is repository for API Server

## Features
* API endpoint for statistic values such as mean, max, and min of enrironmental factors when allergic rhinitis happened in the morning.
* API endpoint for statistic values such as mean, max, and min of enrironmental factors and does allergic rhinitis happned from our samples.

## Endpoint
URL for api endpoint
```
http://127.0.0.1:8080/allergic-api/v1/{endpoint}
```
| Endpoint | description|
| -------- | ------- |
| /average_temp| Return the average temperature when allergic rhinitis happened.|
| /average_humid|Return the average humidity when allergic rhinitis happened. |
| /average_aqi|Return the average qai when allergic rhinitis happened. |
| /average_pm10|Return the average pm10 when allergic rhinitis happened. |
| /average_pm25|Return the average pm25 when allergic rhinitis happened. |
| /average_all|Return the average temperature, humidity, aqi, pm10 and pm25 when allergic rhinitis happened. |
| /min_temp| Return the minimum temperature when allergic rhinitis happened.|
| /min_humid|Return the minimum humidity when allergic rhinitis happened. |
| /min_aqi|Return the minimum qai when allergic rhinitis happened. |
| /min_pm10|Return the minimum pm10 when allergic rhinitis happened. |
| /min_pm25|Return the minimum pm25 when allergic rhinitis happened. |
| /min_all|Return the minimum temperature, humidity, aqi, pm10 and pm25 when allergic rhinitis happened. |
| /max_temp| Return the maximum temperature when allergic rhinitis happened.|
| /max_humid|Return the maximum humidity when allergic rhinitis happened. |
| /max_aqi|Return the maximum qai when allergic rhinitis happened. |
| /max_pm10|Return the maximum pm10 when allergic rhinitis happened. |
| /max_pm25|Return the maximum pm25 when allergic rhinitis happened. |
| /max_all|Return the maximum temperature, humidity, aqi, pm10 and pm25 when allergic rhinitis happened. |
| /average_given_date/{date}|Given date in the parameter return average eviropment factor along with does allergic rhinitis happen on that day. |
| /min_given_date/{date}|Given date in the parameter return minimum eviropment factor along with does allergic rhinitis happen on that day. |
| /max_given_date/{date}| Given date in the parameter return maximum eviropment factor along with does allergic rhinitis happen on that day.|

## Required libraries and tools
Python version >= 3.8
### API Server
connexion[swagger-ui]<br>
werkzeug<br>
swagger-ui-bundle<br>
python_dateutil<br>
setuptools<br>
Flask<br>
pymysql<br>
DBUtils<br>

## Building and running
1. Change directory to the API Server directory.
```
cd API-server
```
2. Create virtual environment.
```
python -m venv venv
```
3. Activate virtual environment.
Macos/Linux
```
./venv/bin/activate
```
Windows
```
.\venv\Scripts\activate
```
5. Install the required packages.
```
pip install -r requirements.txt
```
6. Edit config file
```
nvim config.py\ example or use your prefered text editor
```
7. Run API Server
```
python3 app.py
```
8. Open API specification or request API endpoint
```
API specification

http://127.0.0.1:8080/allergic-api/v1/ui/

Request API endpoint

http://127.0.0.1:8080/allergic-api/{endpoint}
```

