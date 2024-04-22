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
            SELECT AVG(aqi)
            FROM (SELECT DATE(ts) as date, aqi
                  FROM pro_aqi
                  WHERE HOUR(ts) >= 4 AND HOUR(ts) < 8
                 ) AS `date_aqi`
            INNER JOIN (
                SELECT DISTINCT date, fare_up
                from pro_fare_up
                where fare_up = TRUE
            ) AS fare_up ON fare_up.date = date_aqi.date
            GROUP BY fare_up.fare_up;
            """)
            return cs.fetchone()[0]

    def get_average_pm10(self):
        with self.pool.connection() as conn, conn.cursor() as cs:
            cs.execute("""
            SELECT AVG(pm10)
            FROM (SELECT DATE(ts) as date, pm10
                  FROM pro_aqi
                  WHERE HOUR(ts) >= 4 AND HOUR(ts) < 8
                 ) AS `date_aqi`
            INNER JOIN (
                SELECT DISTINCT date, fare_up
                from pro_fare_up
                where fare_up = TRUE
            ) AS fare_up ON fare_up.date = date_aqi.date
            GROUP BY fare_up.fare_up;
            """)
            return cs.fetchone()[0]

    def get_average_pm25(self):
        with self.pool.connection() as conn, conn.cursor() as cs:
            cs.execute("""
            SELECT AVG(pm25)
            FROM (SELECT DATE(ts) as date, pm25
                  FROM pro_aqi
                  WHERE HOUR(ts) >= 4 AND HOUR(ts) < 8
                 ) AS `date_aqi`
            INNER JOIN (
                SELECT DISTINCT date, fare_up
                from pro_fare_up
                where fare_up = TRUE
            ) AS fare_up ON fare_up.date = date_aqi.date
            GROUP BY fare_up.fare_up;
            """)
            return cs.fetchone()[0]

    def get_average_all(self):
        with self.pool.connection() as conn, conn.cursor() as cs:
            cs.execute("""
            SELECT AVG(pm25), AVG(pm10), AVG(aqi)
            FROM (SELECT DATE(ts) as date, pm25, pm10, aqi
                  FROM pro_aqi
                  WHERE HOUR(ts) >= 4 AND HOUR(ts) < 8
                 ) AS `date_aqi`
            INNER JOIN (
                SELECT DISTINCT date, fare_up
                from pro_fare_up
                where fare_up = TRUE
            ) AS fare_up ON fare_up.date = date_aqi.date
            GROUP BY fare_up.fare_up;
            """)
            print(cs.fetchone())
