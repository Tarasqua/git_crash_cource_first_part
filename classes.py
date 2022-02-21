"""Класс для представления автомобиля"""


class Car:
    """Простая модель автомобиля"""

    def __init__(self, make, model, year=2010):
        """Инициализирует атрибуты описания автомобиля"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank = 20

    def get_descriptive_name(self):
        """Инициализирует аккуратно отформатированное описание"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Выводит пробег машины в милях"""
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """
        Устанавливает заданное значение на одометре
        При попытке обратной подкрутки изменение отклоняется
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Увеличивает показания одометра с заданным приращением"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        print(f"Tank is {self.gas_tank}")


class Restaurant:
    """Простая модель ресторана."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name.title()} {self.cuisine_type} restaurant"
              f" is waiting for you!")

    def open_restaurant(self):
        print("Restaurant is open.")

    def set_number_served(self, visitors_number):
        self.number_served = visitors_number

    def increment_number_served(self, increment):
        self.number_served += increment


class User:
    """Простая модель пользователя"""

    def __init__(self,
                 first_name,
                 last_name,
                 age,
                 location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        full_name = f"{self.first_name.title()} {self.last_name.title()}"
        print(f"Information about user:"
              f"\n\tname: {full_name}"
              f"\n\tage: {self.age}"
              f"\n\tlocation: {self.location.title()}")

    def greet_user(self):
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Die:
    """Кубик"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        from random import randint
        print(f"You've got {randint(1, self.sides)}")


class AnonymousSurvey():
    """Сбор анонимных ответов на опросы."""

    def __init__(self, question):
        """Сохраняет вопрос и готовится к сохранению ответов."""
        self.question = question
        self.responses = []

    def show_questions(self):
        """Выводит вопрос."""
        print(self.question)

    def store_response(self, new_response):
        """Сохраняет один ответ на опрос."""
        self.responses.append(new_response)

    def show_results(self):
        """Выводит все полученные ответы."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")


class Employee:
    """Представление работника."""

    def __init__(self, name, lastname, salary):
        self.name = name
        self.lastname = lastname
        self.salary = salary

    def salary_raise(self, increase=5000):
        """Увеличивает ежегодный оклад."""
        self.salary += increase

