import numbers

from unittest import TestCase
from database_util import DataBase

class TestDatabaseConnection(TestCase):
    """Test cases focus on database connection and getting result from queries"""

    def setUp(self) -> None:
        self.database = DataBase()
        return super().setUp()

    def test_average_hum(self):
        self.assertIsInstance(self.database.get_average_hum(), numbers.Number)

    def test_average_temp(self):
        self.assertIsInstance(self.database.get_average_temp(), numbers.Number)

    def test_average_aqi(self):
        self.assertIsInstance(self.database.get_average_aqi(), numbers.Number)

    def test_average_pm10(self):
        self.assertIsInstance(self.database.get_average_pm10(), numbers.Number)

    def test_average_pm25(self):
        self.assertIsInstance(self.database.get_average_pm25(), numbers.Number)

    def test_average_all(self):
        for info in self.database.get_average_all():
            self.assertIsInstance(info , numbers.Number)
