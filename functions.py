import json


def make_pizza(size, *toppings):
    """выводит описание питсы"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe following models have been printed")
    for completed_model in completed_models:
        print(completed_model)


def count_words(filename):
    """Подсчет приблизительного количества слов в файле."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"Sorry, the file {filename} does not exist.")
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words")


def sum_numbers():
    """Считает сумму двух числел"""
    try:
        first_number = float(input("Введите первое число: "))
        second_number = float(input("Введите второе число: "))
    except ValueError:
        print("Одно из введенных значений не является числом!")
    else:
        print(f"Сумма двух чисел: {round(first_number + second_number, 3)}")


def try_read(filename):
    """Пытается прочитать и вывести содержимое файлов"""
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
        # print(f"File {filename} doesn't exist.")
    else:
        print(contents, '\n')


def try_count_the(filename):
    """Считает количество the"""
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"File {filename} does not exist.")
    else:
        print(f"Number of 'the':{contents.lower().count('the ')}")


# Программа загружает имя пользователя, если оно было сохранено ранее.
# В противном случае она запрашивает имя пользователя и сохраняет его.
def get_stored_username(filename):
    """Получает хранимое имя пользователя, если оно существует."""
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    except json.decoder.JSONDecodeError:
        return None
    else:
        return username


def get_new_username(filename):
    """Запрашивает новое имя пользователя"""
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username.title(), f)
    return username


def mistake_name(filename):
    """В случае смены пользователя, запоминаем нового"""
    username = get_new_username(filename)
    print(f"We'll remember you when you come back, {username.title()}")


def greet_user(filename):
    """Приветствует пользователя по имени"""
    username = get_stored_username(filename)
    if username:
        while True:
            correct_name = input(f"Is your name {username}, isn't it? (yes/no): ")
            if correct_name == 'yes':
                print(f"Welcome back, {username}")
                break
            elif correct_name == 'no':
                mistake_name(filename)
                break
            else:
                print("Please, try one more time.")
    else:
        mistake_name(filename)


# Тесты
def get_formatted_name(first, last, middle=''):
    """Строит отформатированное полное имя."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()


def city_country(city, country, population=''):
    """Строит отформатированное полное название города."""
    if population:
        full_name = f"{city.title()}, {country.title()} - population {population}"
    else:
        full_name = f"{city}, {country}".title()
    return full_name