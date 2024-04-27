import pymysql
from dbutils.pooled_db import PooledDB
from swagger_server.config import DB_HOST, DB_USER, DB_PASSWD, DB_NAME


class DataBase:

    def __init__(self) -> None:
        self.pool = self.__create_pool()

    def __create_pool(self):
        pool = PooledDB(creator=pymysql,
                        host=DB_HOST,
                        user=DB_USER,
                        password=DB_PASSWD,
                        database=DB_NAME,
                        maxconnections=1,
                        blocking=True)
        return pool

    def get_average_temp(self):
        with self.pool.connection() as conn, conn.cursor() as cs:
            cs.execute("""
            SELECT AVG(temperature)
            FROM (SELECT DATE(ts) as date, temperature
                FROM pro_temp_humid
                WHERE HOUR(ts) >= 4 AND HOUR(ts) < 8
            ) AS `date_temp_hu`
            INNER JOIN (
                SELECT DISTINCT date, fare_up
                from pro_fare_up
                where fare_up = TRUE
            ) AS fare_up ON fare_up.date = date_temp_hu.date
            GROUP BY fare_up;
            """)
            return cs.fetchone()[0]
           
    def get_average_hum(self):
        with self.pool.connection() as conn, conn.cursor() as cs:
            cs.execute("""
            SELECT AVG(humidity)
            FROM (SELECT DATE(ts) as date, humidity
                FROM pro_temp_humid
                WHERE HOUR(ts) >= 4 AND HOUR(ts) < 8
            ) AS `date_temp_hu`
            INNER JOIN (
                SELECT DISTINCT date, fare_up
                from pro_fare_up
                where fare_up = TRUE
            ) AS fare_up ON fare_up.date = date_temp_hu.date
            GROUP BY fare_up;
            """)
            return cs.fetchone()[0]
           
    def get_average_aqi(self):
        with self.pool.connection() as conn, conn.cursor() as cs:
            cs.execute("""
            SELECT avg(avg_aqi)
            from (
                SELECT DISTINCT date, fare_up
                FROM pro_fare_up
                WHERE fare_up = TRUE) AS uqi_fare_up
            INNER JOIN (
                SELECT DATE(ts) as date, AVG(aqi) as avg_aqi
                FROM pro_aqi
                WHERE HOUR(ts) >= 4 AND HOUR(ts) < 8
                GROUP BY date
            ) AS date_avg_aqi ON date_avg_aqi.date = uqi_fare_up.date
            GROUP BY uqi_fare_up.fare_up;
            """)
            return cs.fetchone()[0]

    def get_average_pm10(self):
        with self.pool.connection() as conn, conn.cursor() as cs:
            cs.execute("""
            SELECT avg(avg_pm10)
            from (
                SELECT DISTINCT date, fare_up
                FROM pro_fare_up
                WHERE fare_up = TRUE) AS uqi_fare_up
            INNER JOIN (
                SELECT DATE(ts) as date, AVG(pm10) as avg_pm10
                FROM pro_aqi
                WHERE HOUR(ts) >= 4 AND HOUR(ts) < 8
                GROUP BY date
            ) AS date_avg_pm10 ON date_avg_pm10.date = uqi_fare_up.date
            GROUP BY uqi_fare_up.fare_up;
            """)
            return cs.fetchone()[0]

    def get_average_pm25(self):
        with self.pool.connection() as conn, conn.cursor() as cs:
            cs.execute("""
            SELECT avg(avg_pm25)
            from (
                SELECT DISTINCT date, fare_up
                FROM pro_fare_up
                WHERE fare_up = TRUE) AS uqi_fare_up
            INNER JOIN (
                SELECT DATE(ts) as date, AVG(pm25) as avg_pm25
                FROM pro_aqi
                WHERE HOUR(ts) >= 4 AND HOUR(ts) < 8
                GROUP BY date
            ) AS date_avg_pm25 ON date_avg_pm25.date = uqi_fare_up.date
            GROUP BY uqi_fare_up.fare_up;
            """)
            return cs.fetchone()[0]

    def get_average_all(self):
        with self.pool.connection() as conn, conn.cursor() as cs:
            cs.execute("""
            SELECT avg(avg_aqi), avg(avg_pm10), avg(avg_pm25), avg(avg_temp), avg(avg_humid)
            FROM (SELECT DISTINCT date, fare_up
                FROM pro_fare_up
                WHERE fare_up = TRUE) AS uqi_fare_up
            INNER JOIN (
                SELECT DATE(ts) as date, AVG(aqi) as avg_aqi, AVG(pm10) as avg_pm10, AVG(pm25) as avg_pm25
                FROM pro_aqi
                WHERE HOUR(ts) >= 4 AND HOUR(ts) < 8
                GROUP BY date
            ) AS date_avg_aqi ON date_avg_aqi.date = uqi_fare_up.date
            INNER JOIN (
                SELECT DATE(ts) as date, AVG(temperature) as avg_temp, AVG(humidity) as avg_humid
                FROM pro_temp_humid
                WHERE HOUR(ts) >= 4 AND HOUR(ts) < 8
                GROUP BY date
            ) AS date_avg_temp ON date_avg_temp.date = uqi_fare_up.date
            GROUP BY uqi_fare_up.fare_up;
            """)
