# Логирование бегуновн
class Runner:
    def __init__(self, name: str, speed: float):
        if not isinstance(name, str):
            raise TypeError("name должен быть строкой")
        if speed < 0:
            raise ValueError("speed не может быть отрицательным")

        self.name = name
        self.speed = speed

    def run(self):
        return f"{self.name} бежит со скоростью {self.speed} км/ч"


import logging
import unittest

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    filemode='w',  # Исправлено на filemode
    filename='runner_tests.log',
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class Runner:
    def __init__(self, name: str, speed: float):
        if not isinstance(name, str):
            raise TypeError("name должен быть строкой")
        if speed < 0:
            raise ValueError("speed не может быть отрицательным")

        self.name = name
        self.speed = speed

    def run(self):
        return f"{self.name} бежит со скоростью {self.speed} км/ч"


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner("Бегун", -10)  # Передаем отрицательное значение speed
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", e)
        else:
            logging.info('"test_walk" выполнен успешно')

    def test_run(self):
        try:
            runner = Runner(12345, 10)  # Передаем не строку в name
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", e)
        else:
            logging.info('"test_run" выполнен успешно')


if __name__ == '__main__':
    unittest.main()