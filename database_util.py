import pymysql
from dbutils.pooled_db import PooledDB
from config import DB_HOST, DB_USER, DB_PASSWD, DB_NAME


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

# average
    def get_average_temp(self):
        with self.pool.connection() as conn, conn.cursor() as cs:
            cs.execute("""
            SELECT AVG(temperature)
            FROM (SELECT DATE(ts) as date, temperature
                FROM temp_humid
                WHERE HOUR(ts) >= 5 AND HOUR(ts) <= 8
            ) AS `date_temp_hu`
            INNER JOIN (
                SELECT DISTINCT date, flare_up
                from flare_up
                where flare_up = TRUE
            ) AS flare_up ON flare_up.date = date_temp_hu.date
            GROUP BY flare_up;
            """)
            return cs.fetchone()[0]
           
    def get_average_hum(self):
        with self.pool.connection() as conn, conn.cursor() as cs:
            cs.execute("""
            SELECT AVG(humidity)
            FROM (SELECT DATE(ts) as date, humidity
                FROM temp_humid
                WHERE HOUR(ts) >= 5 AND HOUR(ts) <= 8
            ) AS `date_temp_hu`
            INNER JOIN (
                SELECT DISTINCT date, flare_up
                from flare_up
                where flare_up = TRUE
            ) AS flare_up ON flare_up.date = date_temp_hu.date
            GROUP BY flare_up;
            """)
            return cs.fetchone()[0]
           
    def get_average_aqi(self):
        with self.pool.connection() as conn, conn.cursor() as cs:
            cs.execute("""
            SELECT avg(avg_aqi)
            from (
                SELECT DISTINCT date, flare_up
                FROM flare_up
                WHERE flare_up = TRUE) AS uqi_fare_up
            INNER JOIN (
                SELECT DATE(ts) as date, AVG(aqi) as avg_aqi
                FROM aqi
                WHERE HOUR(ts) >= 5 AND HOUR(ts) <= 8
                GROUP BY date
            ) AS date_avg_aqi ON date_avg_aqi.date = uqi_fare_up.date
            GROUP BY uqi_fare_up.flare_up;
            """)
            return cs.fetchone()[0]

    def get_average_pm10(self):
        with self.pool.connection() as conn, conn.cursor() as cs:
            cs.execute("""
            SELECT avg(avg_pm10)
            from (
                SELECT DISTINCT date, flare_up
                FROM flare_up
                WHERE flare_up = TRUE) AS uqi_fare_up
            INNER JOIN (
                SELECT DATE(ts) as date, AVG(pm10) as avg_pm10
                FROM aqi
                WHERE HOUR(ts) >= 5 AND HOUR(ts) <= 8
                GROUP BY date
            ) AS date_avg_pm10 ON date_avg_pm10.date = uqi_fare_up.date
            GROUP BY uqi_fare_up.flare_up;
            """)
            return cs.fetchone()[0]

    def get_average_pm25(self):
        with self.pool.connection() as conn, conn.cursor() as cs:
            cs.execute("""
            SELECT avg(avg_pm25)
            from (
                SELECT DISTINCT date, flare_up
                FROM flare_up
                WHERE flare_up = TRUE) AS uqi_fare_up
            INNER JOIN (
                SELECT DATE(ts) as date, AVG(pm25) as avg_pm25
                FROM aqi
                WHERE HOUR(ts) >= 5 AND HOUR(ts) <= 8
                GROUP BY date
            ) AS date_avg_pm25 ON date_avg_pm25.date = uqi_fare_up.date
            GROUP BY uqi_fare_up.flare_up;
            """)
            return cs.fetchone()[0]

    def get_average_all(self):
        with self.pool.connection() as conn, conn.cursor() as cs:
            cs.execute("""
            SELECT avg(avg_aqi), avg(avg_pm10), avg(avg_pm25), avg(avg_temp), avg(avg_humid)
            FROM (SELECT DISTINCT date, flare_up
                FROM flare_up
                WHERE flare_up = TRUE) AS uqi_fare_up
            INNER JOIN (
                SELECT DATE(ts) as date, AVG(aqi) as avg_aqi, AVG(pm10) as avg_pm10, AVG(pm25) as avg_pm25
                FROM aqi
                WHERE HOUR(ts) >= 5 AND HOUR(ts) <= 8
                GROUP BY date
            ) AS date_avg_aqi ON date_avg_aqi.date = uqi_fare_up.date
            INNER JOIN (
                SELECT DATE(ts) as date, AVG(temperature) as avg_temp, AVG(humidity) as avg_humid
                FROM temp_humid
                WHERE HOUR(ts) >= 5 AND HOUR(ts) <= 8
                GROUP BY date
            ) AS date_avg_temp ON date_avg_temp.date = uqi_fare_up.date
            GROUP BY uqi_fare_up.flare_up;
            """)
            return cs.fetchone()
# minimum
    def get_min_temp(self):
        with self.pool.connection() as conn, conn.cursor() as cs:
            cs.execute("""
            SELECT MIN(temperature)
            FROM (SELECT DATE(ts) as date, temperature
                FROM temp_humid
                WHERE HOUR(ts) >= 5 AND HOUR(ts) <= 8
            ) AS `date_temp_hu`
            INNER JOIN (
                SELECT DISTINCT date, flare_up
                from flare_up
                where flare_up = TRUE
            ) AS flare_up ON flare_up.date = date_temp_hu.date
            GROUP BY flare_up;
            """)
            return cs.fetchone()[0]
           
    def get_min_hum(self):
        with self.pool.connection() as conn, conn.cursor() as cs:
            cs.execute("""
            SELECT MIN(humidity)
            FROM (SELECT DATE(ts) as date, humidity
                FROM temp_humid
                WHERE HOUR(ts) >= 5 AND HOUR(ts) <= 8
            ) AS `date_temp_hu`
            INNER JOIN (
                SELECT DISTINCT date, flare_up
                from flare_up
                where flare_up = TRUE
            ) AS flare_up ON flare_up.date = date_temp_hu.date
            GROUP BY flare_up;
            """)
            return cs.fetchone()[0]
           
    def get_min_aqi(self):
        with self.pool.connection() as conn, conn.cursor() as cs:
            cs.execute("""
            SELECT MIN(avg_aqi)
            from (
                SELECT DISTINCT date, flare_up
                FROM flare_up
                WHERE flare_up = TRUE) AS uqi_fare_up
            INNER JOIN (
                SELECT DATE(ts) as date, AVG(aqi) as avg_aqi
                FROM aqi
                WHERE HOUR(ts) >= 5 AND HOUR(ts) <= 8
                GROUP BY date
            ) AS date_avg_aqi ON date_avg_aqi.date = uqi_fare_up.date
            GROUP BY uqi_fare_up.flare_up;
            """)
            return cs.fetchone()[0]

    def get_min_pm10(self):
        with self.pool.connection() as conn, conn.cursor() as cs:
            cs.execute("""
            SELECT MIN(avg_pm10)
            from (
                SELECT DISTINCT date, flare_up
                FROM flare_up
                WHERE flare_up = TRUE) AS uqi_fare_up
            INNER JOIN (
                SELECT DATE(ts) as date, AVG(pm10) as avg_pm10
                FROM aqi
                WHERE HOUR(ts) >= 5 AND HOUR(ts) <= 8
                GROUP BY date
            ) AS date_avg_pm10 ON date_avg_pm10.date = uqi_fare_up.date
            GROUP BY uqi_fare_up.flare_up;
            """)
            return cs.fetchone()[0]

    def get_min_pm25(self):
        with self.pool.connection() as conn, conn.cursor() as cs:
            cs.execute("""
            SELECT MIN(avg_pm25)
            from (
                SELECT DISTINCT date, flare_up
                FROM flare_up
                WHERE flare_up = TRUE) AS uqi_fare_up
            INNER JOIN (
                SELECT DATE(ts) as date, AVG(pm25) as avg_pm25
                FROM aqi
                WHERE HOUR(ts) >= 5 AND HOUR(ts) <= 8
                GROUP BY date
            ) AS date_avg_pm25 ON date_avg_pm25.date = uqi_fare_up.date
            GROUP BY uqi_fare_up.flare_up;
            """)
            return cs.fetchone()[0]

    def get_min_all(self):
        with self.pool.connection() as conn, conn.cursor() as cs:
            cs.execute("""
            SELECT min(avg_aqi), min(avg_pm10), min(avg_pm25), min(avg_temp), min(avg_humid)
            FROM (SELECT DISTINCT date, flare_up
                FROM flare_up
                WHERE flare_up = TRUE) AS uqi_fare_up
            INNER JOIN (
                SELECT DATE(ts) as date, AVG(aqi) as avg_aqi, AVG(pm10) as avg_pm10, AVG(pm25) as avg_pm25
                FROM aqi
                WHERE HOUR(ts) >= 5 AND HOUR(ts) <= 8
                GROUP BY date
            ) AS date_avg_aqi ON date_avg_aqi.date = uqi_fare_up.date
            INNER JOIN (
                SELECT DATE(ts) as date, AVG(temperature) as avg_temp, AVG(humidity) as avg_humid
                FROM temp_humid
                WHERE HOUR(ts) >= 5 AND HOUR(ts) <= 8
                GROUP BY date
            ) AS date_avg_temp ON date_avg_temp.date = uqi_fare_up.date
            GROUP BY uqi_fare_up.flare_up;
            """)
            return cs.fetchone()

# maximum

    def get_max_temp(self):
        with self.pool.connection() as conn, conn.cursor() as cs:
            cs.execute("""
            SELECT MAX(temperature)
            FROM (SELECT DATE(ts) as date, temperature
                FROM temp_humid
                WHERE HOUR(ts) >= 5 AND HOUR(ts) <= 8
            ) AS `date_temp_hu`
            INNER JOIN (
                SELECT DISTINCT date, flare_up
                from flare_up
                where flare_up = TRUE
            ) AS flare_up ON flare_up.date = date_temp_hu.date
            GROUP BY flare_up;
            """)
            return cs.fetchone()[0]
           
    def get_max_hum(self):
        with self.pool.connection() as conn, conn.cursor() as cs:
            cs.execute("""
            SELECT MAX(humidity)
            FROM (SELECT DATE(ts) as date, humidity
                FROM temp_humid
                WHERE HOUR(ts) >= 5 AND HOUR(ts) <= 8
            ) AS `date_temp_hu`
            INNER JOIN (
                SELECT DISTINCT date, flare_up
                from flare_up
                where flare_up = TRUE
            ) AS flare_up ON flare_up.date = date_temp_hu.date
            GROUP BY flare_up;
            """)
            return cs.fetchone()[0]
           
    def get_max_aqi(self):
        with self.pool.connection() as conn, conn.cursor() as cs:
            cs.execute("""
            SELECT MAX(avg_aqi)
            from (
                SELECT DISTINCT date, flare_up
                FROM flare_up
                WHERE flare_up = TRUE) AS uqi_fare_up
            INNER JOIN (
                SELECT DATE(ts) as date, AVG(aqi) as avg_aqi
                FROM aqi
                WHERE HOUR(ts) >= 5 AND HOUR(ts) <= 8
                GROUP BY date
            ) AS date_avg_aqi ON date_avg_aqi.date = uqi_fare_up.date
            GROUP BY uqi_fare_up.flare_up;
            """)
            return cs.fetchone()[0]

    def get_max_pm10(self):
        with self.pool.connection() as conn, conn.cursor() as cs:
            cs.execute("""
            SELECT MAX(avg_pm10)
            from (
                SELECT DISTINCT date, flare_up
                FROM flare_up
                WHERE flare_up = TRUE) AS uqi_fare_up
            INNER JOIN (
                SELECT DATE(ts) as date, AVG(pm10) as avg_pm10
                FROM aqi
                WHERE HOUR(ts) >= 5 AND HOUR(ts) <= 8
                GROUP BY date
            ) AS date_avg_pm10 ON date_avg_pm10.date = uqi_fare_up.date
            GROUP BY uqi_fare_up.flare_up;
            """)
            return cs.fetchone()[0]

    def get_max_pm25(self):
        with self.pool.connection() as conn, conn.cursor() as cs:
            cs.execute("""
            SELECT MAX(avg_pm25)
            from (
                SELECT DISTINCT date, flare_up
                FROM flare_up
                WHERE flare_up = TRUE) AS uqi_fare_up
            INNER JOIN (
                SELECT DATE(ts) as date, AVG(pm25) as avg_pm25
                FROM aqi
                WHERE HOUR(ts) >= 5 AND HOUR(ts) <= 8
                GROUP BY date
            ) AS date_avg_pm25 ON date_avg_pm25.date = uqi_fare_up.date
            GROUP BY uqi_fare_up.flare_up;
            """)
            return cs.fetchone()[0]

    def get_max_all(self):
        with self.pool.connection() as conn, conn.cursor() as cs:
            cs.execute("""
            SELECT max(avg_aqi), max(avg_pm10), max(avg_pm25), max(avg_temp), max(avg_humid)
            FROM (SELECT DISTINCT date, flare_up
                FROM flare_up
                WHERE flare_up = TRUE) AS uqi_fare_up
            INNER JOIN (
                SELECT DATE(ts) as date, AVG(aqi) as avg_aqi, AVG(pm10) as avg_pm10, AVG(pm25) as avg_pm25
                FROM aqi
                WHERE HOUR(ts) >= 5 AND HOUR(ts) <= 8
                GROUP BY date
            ) AS date_avg_aqi ON date_avg_aqi.date = uqi_fare_up.date
            INNER JOIN (
                SELECT DATE(ts) as date, AVG(temperature) as avg_temp, AVG(humidity) as avg_humid
                FROM temp_humid
                WHERE HOUR(ts) >= 5 AND HOUR(ts) <= 8
                GROUP BY date
            ) AS date_avg_temp ON date_avg_temp.date = uqi_fare_up.date
            GROUP BY uqi_fare_up.flare_up;
            """)
            return cs.fetchone()
# withdate
    def get_min_all_with_date(self, date):
        with self.pool.connection() as conn, conn.cursor() as cs:
            cs.execute("""
            SELECT min(avg_aqi), min(avg_pm10), min(avg_pm25), min(avg_temp), min(avg_humid), uqi_fare_up.date, sum(flare_up)
            FROM (SELECT date, flare_up
                FROM flare_up
                ) AS uqi_fare_up
            INNER JOIN (
                SELECT DATE(ts) as date, AVG(aqi) as avg_aqi, AVG(pm10) as avg_pm10, AVG(pm25) as avg_pm25
                FROM aqi
                WHERE HOUR(ts) >= 5 AND HOUR(ts) <= 8
                GROUP BY date
            ) AS date_avg_aqi ON date_avg_aqi.date = uqi_fare_up.date
            INNER JOIN (
                SELECT DATE(ts) as date, AVG(temperature) as avg_temp, AVG(humidity) as avg_humid
                FROM temp_humid
                WHERE HOUR(ts) >= 5 AND HOUR(ts) <= 8
                GROUP BY date
            ) AS date_avg_temp ON date_avg_temp.date = uqi_fare_up.date
            where uqi_fare_up.date = %s
            group by date;
            """, [date])
            return cs.fetchone()

    def get_max_all_with_date(self, date):
        with self.pool.connection() as conn, conn.cursor() as cs:
            cs.execute("""
            SELECT max(avg_aqi), max(avg_pm10), max(avg_pm25), max(avg_temp), max(avg_humid), uqi_fare_up.date, sum(flare_up)
            FROM (SELECT date, flare_up
                FROM flare_up
                ) AS uqi_fare_up
            INNER JOIN (
                SELECT DATE(ts) as date, AVG(aqi) as avg_aqi, AVG(pm10) as avg_pm10, AVG(pm25) as avg_pm25
                FROM aqi
                WHERE HOUR(ts) >= 5 AND HOUR(ts) <= 8
                GROUP BY date
            ) AS date_avg_aqi ON date_avg_aqi.date = uqi_fare_up.date
            INNER JOIN (
                SELECT DATE(ts) as date, AVG(temperature) as avg_temp, AVG(humidity) as avg_humid
                FROM temp_humid
                WHERE HOUR(ts) >= 5 AND HOUR(ts) <= 8
                GROUP BY date
            ) AS date_avg_temp ON date_avg_temp.date = uqi_fare_up.date
            where uqi_fare_up.date = %s
            group by date;
            """, [date])
            return cs.fetchone()

    def get_average_all_with_date(self, date):
        with self.pool.connection() as conn, conn.cursor() as cs:
            cs.execute("""
            SELECT avg(avg_aqi), avg(avg_pm10), avg(avg_pm25), avg(avg_temp), avg(avg_humid), uqi_fare_up.date, sum(flare_up)
            FROM (SELECT date, flare_up
                FROM flare_up
                ) AS uqi_fare_up
            INNER JOIN (
                SELECT DATE(ts) as date, AVG(aqi) as avg_aqi, AVG(pm10) as avg_pm10, AVG(pm25) as avg_pm25
                FROM aqi
                WHERE HOUR(ts) >= 5 AND HOUR(ts) <= 8
                GROUP BY date
            ) AS date_avg_aqi ON date_avg_aqi.date = uqi_fare_up.date
            INNER JOIN (
                SELECT DATE(ts) as date, AVG(temperature) as avg_temp, AVG(humidity) as avg_humid
                FROM temp_humid
                WHERE HOUR(ts) >= 5 AND HOUR(ts) <= 8
                GROUP BY date
            ) AS date_avg_temp ON date_avg_temp.date = uqi_fare_up.date
            where uqi_fare_up.date = %s
            group by date;
            """, [date])
            return cs.fetchone()
