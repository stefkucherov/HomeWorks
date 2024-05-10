"""
Программа с классом Car. При инициализации объекта ему
должны задаваться атрибуты color, type и year. Реализовать
пять методов. Запуск автомобиля – выводит строку
«Автомобиль заведён». Отключение автомобиля – выводит
строку «Автомобиль заглушен». Методы для присвоения
автомобилю года выпуска, типа и цвета.
"""


class Car:
    def __init__(self, color, car_type, year):
        self.color = color
        self.type = car_type
        self.year = year
        self.engine_started = False

    def start_engine(self):
        self.engine_started = True
        print("Автомобиль заведён.")

    def stop_engine(self):
        self.engine_started = False
        print("Автомобиль заглушен.")

    def get_info(self):
        engine_status = "Заведен" if self.engine_started else "Заглушен"
        print(f"{self.color} {self.type} {self.year}({engine_status})")


my_car = Car(color="Красный", car_type="седан", year=2022)

my_car.get_info()
my_car.start_engine()
my_car.get_info()
