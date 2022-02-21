"""Набор классов для прдставления электромобилей"""
from classes import Car, Restaurant, User

class Battery:
    """Простая модель аккумулятора автомобиля"""

    def __init__(self, battery_size=75):
        """Инициализирует атрибуты аккумулятора"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Выводит приблизительный запас хода для аккумулятора."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge")

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100


class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""

    def __init__(self, make, model, year):
        """
        Ининциализирует атрибуты дочернего класса
        Затем инициализирует атрибуты, специфические для электромобиля
        """
        super().__init__(make, model, year)
        self.battery_size = 75
        self.battery = Battery()

    def fill_gas_tank(self):
        """У электромобилей нет бензобака"""
        print("This car doesn't have a gas tank!")


class IceCreamStand(Restaurant):
    """Особая разновидность ресторанов"""

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def input_flavor(self):
        while True:
            flavor = input("Input flavor: ")
            if flavor == "":
                break
            else:
                self.flavors.append(flavor)

    def output_flavors(self):
        print("We have different flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")


class Admin(User):
    """Особая разновидность пользователя"""

    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()


class Privileges:
    """Простая модель привелегий"""

    def __init__(self):
        self.privileges = ["Разрешено добавлять сообщения",
                           "Разрешено удалять пользователей",
                           "Разрешено банить пользователей"]

    def show_privileges(self):
        print(f"Набор привелегий:")
        for privilege in self.privileges:
            print(f"-{privilege}")