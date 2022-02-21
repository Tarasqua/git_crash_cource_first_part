# # Инициализируем цитату и имя
# quote = 'ones said, "A person who never made\na mistake never tried anything new."'
# famous_person = "  Albert Einstein   "
# # Формируем сообщение
# message = f"{famous_person} {quote}"
# # Выводим сообщение
# print(f"|{famous_person.rstrip()}|\n"
#       f"|{famous_person.lstrip()}|\n"
#       f"|\t{famous_person.strip()}|")
# import this

# while True: print(eval(input(">>>")))

# rides = ['Porsche', 'Mercedes', 'BNW', 'Audi']
# print(rides)
# rides.append('Honda')
# print(rides)
# rides.insert(0,'Lada')
# print(rides)
# del rides[-1]
# print(rides)
# popped_ride = rides.pop(2)
# too_exppensive = 'porsche'.title()
# rides.remove(too_exppensive)
# print(f"A ride {too_exppensive} is too expensive for me")
# print(popped_ride)

# invites = ['Mercury', 'Halford', 'Dio']
# print(f"Dear {invites[0]}, I'd like to invite u to dinner with us!")
# print(f"Dear {invites[1]}, I'd like to invite u to dinner with us!")
# print(f"Dear {invites[2]}, I'd like to invite u to dinner with us!")
# print("Halford")
# invites[invites.index('Halford')] = "Hammet"
# print(f"Dear {invites[invites.index('Hammet')]}, I'd like to invite u to dinner with us!")
# invites.insert(0,'Iommi')
# invites.insert(2, 'Batler')
# invites.append('Appice')
# print(invites)
# first_deleted = invites.pop(1)
# second_deleted = invites.pop(2)
# third_deleted = invites.pop(0)
# fourth_deleted = invites.pop(0)
# print(invites)
# del invites[0]
# del invites[0]
# print(invites)

# blackSabbath = ["iommi", "batler", "dio", "appice"]
# print("Original:")
# print(blackSabbath)
# print("Sorted:")
# print(sorted(blackSabbath))
# print("Original again:")
# print(blackSabbath)
# blackSabbath.reverse()
# print(blackSabbath)
# print(len(blackSabbath))

# countries = ['germany', 'poland', 'england', 'france', 'japan']
# print(countries)
# print(sorted(countries))
# print(countries)
# print(sorted(countries, reverse=True))
# print(countries)
# countries.reverse()
# print(countries)
# countries.reverse()
# print(countries)
# countries.sort()
# print(countries)
# countries.sort(reverse=True)
# print(countries)

# rivers = ["volga", "seym", "klyazma", "moskva", "ind", "gang"]
# rivers[len(rivers) - 1] = 'doneck'
# rivers.append('enisey')
# rivers.insert(2, 'lena')
# print(rivers)
# del rivers[2]
# print(rivers)
# popped_rever = rivers.pop(-1)
# rivers.remove('Seym'.lower())
# print(rivers)
# print(sorted(rivers))
# rivers.sort(reverse=True)
# print(rivers)
# print(rivers[len(rivers) - 3])
# print(rivers[-3])

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")
# print("Thank you, everyone. That was a great magic show!")

# pizzas = ['pepperoni', '4 cheeses', 'margarita', 'calzone']
# for pizza in pizzas:
#     print(f"I like {pizza} pizza")
# print("\nI really love pizza!")

# animals = ['cat', 'tiger', 'cougar', 'puma']
# for animal in animals:
#     print(f"{animal} one of cats family")
# print("Any of these animals would be a great pet!")

# squares = [value**2 for value in range(1, 11)]
# print(squares)

# for num in range(1, 21):
#     if num == 20:
#         print(num)
#     else:
#         print(num, end=', ')

# cubes = [value**3 for value in range(1, 11)]
# print(cubes)
# cubes = [value**3 for value in range(10, 21)]
# print(cubes)

# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print("Here are the first three players on my team:")
# for player in players[:3]:
#     print(player.title())
# players_2 = players[:]
# print(players_2)

# myFoods = ['pizza', 'falafel', 'carrot cake', 'french meat', 'fried chicken', 'cola', 'vaffels']
# friendFoods = myFoods[:]
# myFoods.append('cannoli')
# friendFoods.append('ice cream')
# print("My favourite foods are:")
# print(myFoods)
# print("\nMy friend's favourite foods are:")
# print(friendFoods)
# # Первые три элемента
# print(f"The first three items in the list are: {myFoods[:3]}")
# # Средние три
# print(f"Three items from the middle of the list are: {myFoods[int(len(myFoods)/2 - 1):int(len(myFoods)/2 + 2)]}")
# # Последние три
# print(f"The last three items in the list are: {myFoods[-3:]}")

# myPizzas = ['pepperoni', 'margarita', 'calzone', 'focaccia']
# friendsPizzas = myPizzas[:]
# myPizzas.append('crudo')
# friendsPizzas.append('napoletana')
# print("My favourite pizzas are:", end=" ")
# for pizza in myPizzas:
#     if pizza != myPizzas[-1]:
#         print(f"{pizza}, ", end="")
#     else:
#         print(f"{pizza}.")
# print("My friend's favourite pizzas are:", end=" ")
# for friendPizza in friendsPizzas:
#     if friendPizza != friendsPizzas[-1]:
#         print(f"{friendPizza}, ", end="")
#     else:
#         print(f"{friendPizza}.")

# # Кортежи
# dimensions = (200, 50)
# my_t = (3, )
# print("Original dimensions:")
# for dimension in dimensions:
#     print(dimension)
# dimensions = 400, 100
# print("\nModified dimensions:")
# for d in dimensions:
#     print(d)

# cars = ['audi', 'bmw', 'subaru', 'toyota', 'gmc']
# for car in cars:
#     if car == 'bmw' or car == 'gmc':
#         print(car.upper())
#     else:
#         print(car.title())
#
# if 'lada' in cars:
#     print('yes')
# else:
#     print('no')

# banned_users = ['andrew', 'mark', 'george']
# user = 'sofia'
# if user not in banned_users:
#     print(f"{user.title()}, you can post a response if you wish")

# game_active = True
# can_edit = False
# if game_active:
#     print("Let's play!")
# if not can_edit:
#     print("You can't edit the information")
#
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')

# a = 5
# b = 2
# print(a == b)
# m = 'mAx'
# n = 'MaX'
# print(m.lower() == n.lower())
# people = 'kirill', 'sofia', 'george', 'vlad'
# if 'kirill' in people:
#     print('yes')
# if 'danya' not in people:
#     print('yes')

# age = 70
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# elif age < 65:
#     price = 40
# else:
#     price = 20
# print(f'Your admission cost is {price}$')

# alien_color = 'red'
# if alien_color == 'green':
#     print("You've got 5 points")
# elif alien_color == 'yellow':
#     print("You've got 10 points")
# elif alien_color == 'red':
#     print("You've got 15 points")

# age = int(input("Введите возраст: "))
# if age < 2:
#     print('Младенец')
# elif age < 4:
#     print('Малыш')
# elif age < 13:
#     print('Ребенок')
# elif age < 20:
#     print('Подросток')
# elif age < 65:
#     print('Взрослый')
# else:
#     print('Пожилой')

# favourite_fruits = ['banana', 'mango', 'apple']
# if 'banana' in favourite_fruits:
#     print("u really like bananas!")
# if 'orange' not in favourite_fruits:
#     print("well, u don't like oranges")

# request_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for request_topping in request_toppings:
#     if request_topping == 'green peppers':
#         print("Sorry, we are out of green peppers right now.")
#     else:
#         print(f"Adding {request_topping}.")
# print("\nFinished making your pizza!")

# request_toppings = []
# if request_toppings:
#     for request_topping in request_toppings:
#         print(f"Adding {request_topping}.")
#     print("\nFinished making your pizza!")
# else:
#     print("Are you sure want a plain pizza?")

# available_toppings = ['mushrooms', 'olives', 'green peppers',
#                       'pepperoni', 'pineapple', 'extra cheese']
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping in available_toppings:
#         print(f"Adding {requested_topping}.")
#     else:
#         print(f"Sorry, we don't have {requested_topping}")


# # Ввод и проверка пользователей на совместимость (глава 5)
# current_users = ['admin', 'kirill', 'sofia', 'george', 'dos']
# new_users = []
# count = 1
# # Ввод новых
# while True:
#     add_user = input(f"{count}.Input nickname: ")
#     if add_user.lower() not in new_users:
#         new_users.append(add_user)
#         count += 1
#         if count == 5:
#             break
#     else:
#         print("Please, try again\n")
# # Проверка на совпадения
# if current_users or new_users:
#     for current_user in current_users:
#         for index, new_user in enumerate(new_users):
#             while True:
#                 if current_user.lower() == new_user.lower():
#                     new_user = input(f"\nName {current_user} is occupied. Try another name: ")
#                     new_users[index] = new_user
#                 elif current_user.lower() != new_user.lower():
#                     print("Correct name!\n")
#                     break
#     # Соединяем и удаляем массив
#     for i, n in enumerate(new_users):
#         current_users.append(new_users[i])
#     del new_users[:]
#     # Выводим приветствие
#     for current_user in current_users:
#         if current_user == 'admin':
#             print('Hello, admin!')
#         else:
#             print(f"Thank you, {current_user}, for reconnection!")
# elif not new_users:
#     print("There are no new users!")
# else:
#     print("Users list is empty!")


# глава 6
# alien_0 = {'color': 'green', 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])
# new_points = alien_0['points']
# print(f"You just earned {new_points} points!")
# print(alien_0)
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)

# alien_0 = {}
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(f"The alien is {alien_0['color']}")
# alien_0['color'] = 'yellow'
# print(f"The alien is {alien_0['color']}")

# alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast', 'points': 5}
# print(f"Original position: {alien_0['x_position']}")
# # Пришелец перемещается вправо
# # Вычисляем величину смещения на основании текущей скорости
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     # Пришелец двигается быстро
#     x_increment = 3
# # Новая позиция равна сумме старой и приращения
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"New position: {alien_0['x_position']}")
# del alien_0['points']
# print(alien_0)

# favourite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# for name, language in favourite_languages.items():
#     print(f"{name.title()}'s favourite language is {language}")
# for name in favourite_languages.keys():
#     print(name.title())

# alien_0 = {'color': 'green', 'speed': 'slow'}
# point_value = alien_0.get('points', 'No point value assigned.')
# print(point_value)

# human = {'firstname': 'george',
#          'lastname': 'nagiev',
#          'age': 20,
#          'city': 'obninsk',
#          }
# print(human['firstname'])
# print(human['lastname'])
# print(human['age'])
# print(human['city'])

# favourite_numbers = {'george': 7,
#                      'sofia': 3,
#                      'dima': 5,
#                      'mark': 11,
#                      'kirill': 13,
#                      }
# print(f"favourite number of George is {favourite_numbers['george']}")

# dictionary = {
#     'абстракция': 'Абстракция — означает выделение значимой информации и исключение из рассмотрения незначимой.\n'
#                   'С точки зрения программирования - это правильное разделение программы на объекты.\n'
#                   'Абстракция позволяет отобрать главные характеристики и опустить второстепенные.',
#     'инкапсуляция': 'Инкапсуляция — свойство системы, позволяющее объединить данные и методы,\n'
#                     'работающие с ними, в классе.',
#     'наследование': 'Наследование — свойство системы, позволяющее описать новый класс на основе уже существующего\n'
#                     'с частично или полностью заимствующейся функциональностью.',
#     'полиморфизм': 'Полиморфизм — свойство системы использовать объекты с одинаковым интерфейсом без информации\n'
#                    'о типе и внутренней структуре объекта.'
#     }
# print(dictionary['абстракция'])

# user_0 = {'username': 'efermi',
#           'first': 'enrico',
#           'last': 'fermi'
#           }
# for key, value in user_0.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")

# favourite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }
# friends = ['phil', 'sarah']
# for name in sorted(favourite_languages.keys()):
#     print(name.title())
#     if name in friends:
#         language = favourite_languages[name].title()
#         print(f"\t{name.title()}, I see you love {language}!")
# if 'erin' not in favourite_languages.keys():
#     print("\nErin, please take our poll!")
# print("\nThe following languages have been mentioned:")
# for language in set(favourite_languages.values()):
#     print(language.title())

# dictionary = {
#     'абстракция': 'Абстракция — означает выделение значимой информации и исключение из рассмотрения незначимой.\n'
#                   'С точки зрения программирования - это правильное разделение программы на объекты.\n'
#                   'Абстракция позволяет отобрать главные характеристики и опустить второстепенные.',
#     'инкапсуляция': 'Инкапсуляция — свойство системы, позволяющее объединить данные и методы,\n'
#                     'работающие с ними, в классе.',
#     'наследование': 'Наследование — свойство системы, позволяющее описать новый класс на основе уже существующего\n'
#                     'с частично или полностью заимствующейся функциональностью.',
#     'полиморфизм': 'Полиморфизм — свойство системы использовать объекты с одинаковым интерфейсом без информации\n'
#                    'о типе и внутренней структуре объекта.',
#     'класс': 'Класс – это шаблон, описывающий общие свойства группы объектов. Этими свойствами могут быть как \n'
#              'характеристики объектов (размер, вес, цвет и т.п.), так и поведения, роли и т.п.',
#     'атрибут класса': 'Поле (атрибут) класса — это характеристика объекта. Например для фигуры это может быть \n'
#                       'название, площадь, периметр.',
#     }
# for word, definition in dictionary.items():
#     print(f"\nСлово {word.upper()} определяется, как:\n{definition}")

# rivers = {'Egypt': 'neil',
#           'russia': 'volga',
#           'china': 'ind',
#           'ukraine': 'doneck',
#           'belarus': 'pripyat',
#           }
# for name in rivers.values():
#     print(f"River {name.title()}")
# for country in rivers.keys():
#     print(f"Country {country.title()}")

# favourite_languages = {'jen': 'python',
#                        'sarah': 'c',
#                        'edward': 'ruby',
#                        'phil': 'python',
#                        }
# people = ['jen', 'kirill', 'sarah', 'edward', 'phil', 'collin', 'sofia']
# for human in sorted(people):
#     if human in sorted(favourite_languages.keys()):
#         print(f"{human.title()}, thanks")
#     else:
#         print(f"{human.title()}, please")

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)

# # Пустой список для хранения пришельцев
# aliens = []
# # 30 зеленых пришельцев
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
# # Изменяем характеристики первых 3
# for alien in aliens[0:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['points'] = 10
#     elif alien['color'] == 'yellow':
#         alien['color'] = 'red'
#         alien['speed'] = 'fast'
#         alien['points'] = 15
# # Вывод 5 первых пришельцев
# for alien in aliens[:5]:
#     print(alien)
# print("...")
# # Вывод количества созданных пришельцев
# print(f"Total number of aliens: {len(aliens)}")

# # Сохранение информации о заказанной питце
# pizza = {'crust': 'thick',
#          'toppings': ['mushrooms', 'extra cheese']
#          }
# # Описание заказа
# print(f"You ordered a {pizza['crust']}-crust pizza "
#       "with the following toppings:")
# for topping in pizza['toppings']:
#     print("\t" + topping)

# favourite_languages = {'jen': ['python', 'ruby'],
#                        'sarah': ['c'],
#                        'edward': ['ruby', 'go'],
#                        'phil': ['python', 'java'],
#                        }
# for name, languages in favourite_languages.items():
#     if len(languages) > 1:
#         print(f"\n{name.title()}'s favorite languages are:")
#         for language in languages:
#             print(f"\t{language.title()}")
#     else:
#         print(f"\n{name.title()}'s favorite language is:\n\t{languages[0].title()}")

# Вложенный словарь
# users = {'tarasqua':
#              {'first': 'kirill',
#               'last': 'tarasov',
#               'location': 'moscow',
#               },
#          'jora':
#              {'first': 'george',
#               'last': 'nagiev',
#               'location': 'obninsk',
#               }
#          }
# for username, user_info in users.items():
#     print(f"\nUsername: {username}")
#     full_name = f"{user_info['first']} {user_info['last']}"
#     location = user_info['location']
#     print(f"\tFull name: {full_name.title()}")
#     print(f"\tLocation: {location.title()}")

# number = int(input("Input some number: "))
# if number % 2 == 0:
#     print(f"\nThe number {number} is even")
# else:
#     print(f"The number {number} is odd")

# tables = int(input("How many people would you invite? "))
# if tables > 8:
#     print("You've got to wait")
# else:
#     print("There are your places!")

# number = int(input("Number: "))
# if number % 10 == 0:
#     print("Yes!")
# else:
#     print("Nah...")

# prompt = "\nTell me something, and I'll repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program: "
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)

# while True:
#     topping = input("Input topping: ")
#     if topping == 'quit':
#         break
#     print(f"Topping {topping} added in order!\n")

# while True:
#     age = int(input("Input your age ('999' to quit): "))
#     if age < 3:
#         print("Free")
#     elif age < 12:
#         print("$10")
#     elif age > 12 and age != 999:
#         print("$15")
#     elif age == 999:
#         break

# active = True
# while active:
#     topping = input("Input topping: ")
#     if topping == 'quit':
#         active = False
#     else:
#         print(f"Topping {topping} added in order!\n")

# unconfirmed_users = ['kirill', 'sofia', 'george']
# confirmed_users = []
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print(f"Verifying user {current_user.title()}")
#     confirmed_users.append(current_user)
# print("\nThe following users have been confirmed:")
# for c in confirmed_users:
#     print(c.title())

# pets = ['dog', 'cat', 'mouse', 'cat', 'rabbit', 'cat', 'elephant', 'cat', 'camel']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

# responses = {}
# # Установка флага продолжения опроса.
# polling_active = True
# while polling_active:
#     # Запрос имени и ответа пользователя.
#     name = input("\nWhat is your name? ")
#     response = input("Which mountain would you like to climb someday? ")
#     # Ответ сохраняется в словаре:
#     responses[name] = response
#     # Проверка продолжения опроса.
#     repeat = input("Would you like to let another person respond (yes/no)? ")
#     if repeat == 'no':
#         polling_active = False
# # Опрос завершен, вывести результаты.
# print("\n--- Poll results ---")
# for name, response in responses.items():
#     print(f"{name.title()} would like to climb {response.title()}.")

# kirill = {'name': 'kirill', 'height': 180, 'weight': 86}
# george = {'name': 'george', 'height': 178, 'weight': 55}
# people = [kirill, george]
# for man in people:
#     for dimension, value in man.items():
#         if dimension == 'name':
#             print(f"\nName is {value.title()} and his parameters are:")
#         elif dimension == 'height':
#             print(f"\tHeight is {value}")
#         else:
#             print(f"\tWeight is {value}")

# pushok = {'type': 'cat', 'owner': 'kirill'}
# sherstyanoy = {'type': 'dog', 'owner': 'vlad'}
# cary = {'type': 'parrot', 'owner': 'masha'}
# pets = [pushok, sherstyanoy, cary]
# for pet in pets:
#     for key, value in pet.items():
#         if pet == pushok:
#             name = "pushok"
#         elif pet == sherstyanoy:
#             name = "sherstyanoy"
#         else:
#             name = "cary"
#         if key == 'type':
#             type = value
#         elif key == 'owner':
#             owner = value
#     print(f"\n{type.title()} called {name.title()} is {owner.title()}'s pet")

# favourite_places = {'moscow':
#                         {'kirill': ['hovrino', 'tverskaya']},
#                     'cuba':
#                         {'dima': ['doneck', 'koptilnya'],
#                          'george': ['osvencim']}
#                     }
# for favourite_place, man in favourite_places.items():
#     for name, places in man.items():
#         if len(places) > 1:
#             print(f"\n{name.title()}'s favourite places in {favourite_place.title()} are:")
#             for place in places:
#                 print(f"\t{place.title()}")
#         else:
#             print(f"\n{name.title()}'s favourite place in {favourite_place.title()} is \n\t{places[0].title()}")

# cities = {'new york':
#               {'country': 'usa', 'population': 5_000_000, 'fact': 'big apple'},
#           'moscow':
#               {'country': 'russia', 'population': 2_000_000, 'fact': 'native'},
#           'rome':
#               {'country': 'italy', 'population': 1_000_000, 'fact': 'forever'}
#           }
# for city, information in cities.items():
#     print(f"\nThere is {city.title()}."
#           f"\n\tLocation: {information['country'].title()},"
#           f"\n\tPopulation: {information['population']},"
#           f"\n\tFact: {information['fact']}.")

# sandwich_orders = ['shrimp', 'pastrami', 'beef', 'pastrami', 'pork', 'pastrami', 'cheese']
# finished_sandwiches = []
# print("There is no pastrami...\n")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# while sandwich_orders:
#     sandwich = sandwich_orders.pop()
#     print(f"I made your {sandwich}!")
#     finished_sandwiches.append(sandwich)
# print(finished_sandwiches)

# places = {}
# active = True
# while active:
#     if input("Is there somebody wants to take part in our survey? (yes/no) ") == 'yes':
#         name = input("Input your name: ")
#         place = input("Where do you want to spend holidays? ")
#         places[name] = place
#     else:
#         active = False
# for name, place in places.items():
#     print(f"\n{name.title()} wants to spend his holidays in {place.title()}")

# глава 8
# def greet_user(username):
#     """Выводит простое приветствие"""
#     print(f"Hello, {username}")
# greet_user(input("Your name? ").title())

# def display_message(title):
#     print(f"One of my favourite books is {title}")
# display_message(input("Titile: ").title())

# def describe_pet(pet_name, animal_type = 'dog'):
#     """Выводит информацию о животном"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}")
# describe_pet(pet_name=input("Name: "))
# describe_pet(animal_type=input("Type: "), pet_name=input("Name: "))
# describe_pet('Willie')

# def make_shirt(size = 'L', text = 'I love python'):
#     print(f"Shirt {size.title()} size with text pattern: '{text}'")
# make_shirt('m', 'Hello, world!')
# make_shirt(text='Hello world!')
# make_shirt('XL', 'Dima loh')

# def describe_city(name, country = 'Russia'):
#     print(f"{name.title()} is in {country.title()}.")
# describe_city('Kursk')
# describe_city('Moscow')
# describe_city('New York', 'USA')

# def build_person(first_name, last_name, age = None):
#     """Возвращает словарь с информацией о человеке."""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
# musician = build_person('jimi', 'hendrix', 27)
# print(musician)

# def get_formated_name(first_name, last_name, middle_name=""):
#     """Возвращает аккуратно отформатированное полное имя."""
#     if middle_name:
#         fullName = f"{first_name} {middle_name} {last_name}"
#     else:
#         fullName = f"{first_name} {last_name}"
#     return fullName.title()
#
#
# while True:
#     print("\nPlease, tell me your name: "
#           "\n(enter 'q' at any time to quit)")
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break
#     m_name = input("Middle name: ")
#     if m_name == 'q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#     print(f"\nHello, {get_formated_name(f_name, l_name, m_name)}!")

# def city_country(name, country):
#     return f"{name.title()}, {country.title()}"
#
# while True:
#     city = input("Name: ")
#     if city == "":
#         break
#     country = input("Country: ")
#     if country == "":
#         break
#     print(f"\n{city_country(city, country)}")

# def make_album(executor, title):
#     """Создание альбома по исполнителю и названию"""
#     album = {'executor': executor, 'name': title}
#     return album
# judas_priest = make_album('judas priest', 'killing machine')
# guns_n_roses = make_album("guns n' roses", 'appetite for destruction')
# black_sabbath = make_album("black sabbath", "heaven & hell")
# albums = [judas_priest, guns_n_roses, black_sabbath]
# while True:
#     access = input("Do yoy want to add something (yes/no): ")
#     if access == "yes":
#         albums.append(make_album(input("Executor: "), input("Album's title: ")))
#     elif access == "no":
#         break
# # Чтобы выводить пару значений словаря
# k = 1
# for album in albums:
#     for key, value in album.items():
#         if k % 2 != 0:
#             executor = f"I do like {value.title()}"
#             k += 1
#         elif k % 2 == 0:
#             print(f"{executor}'s «{value.title()}» album!")
#             k += 1

# def greet_users(names):
#     """Вывод простого приветствия для каждого пользователя в списке"""
#     for name in names:
#         msg = f"Hello, {name.title()}"
#         print(msg)
# usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)

# # Список моделей, которые необходимо напечатать
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# # Цикл последоваетльно печатает каждую модель до конца списка
# # После печати каждая модель перемещается в список completed_models
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)
# # Вывод всех готовых моделей
# print("\nThe following models have been printed")
# for completed_model in completed_models:
#     print(completed_model)
# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)
# def show_completed_models(completed_models):
#     print("\nThe following models have been printed")
#     for completed_model in completed_models:
#         print(completed_model)
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# # [:] создает копию
# print_models(unprinted_designs[:], completed_models)
# show_completed_models(completed_models)

# def send_messages(messages, sent_messages):
#     while messages:
#         current_message = messages.pop()
#         print(f"\nMessage is '{current_message}'")
#         sent_messages.append(current_message)
# messages = ["I love you", "Good night!", "Honey, good morning"]
# sent_messages = []
# send_messages(messages[:], sent_messages)
# print(messages, sent_messages)

# def make_pizza(size, *toppings):
#     """Вывод списка заказанных топингов"""
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")
# make_pizza(16, 'pepperoni')
# make_pizza(22, 'mushrooms', 'green peppers', 'extra cheese')

# def build_profile(first, last, **user_info):
#     """Строит словарь с информацией о пользователе"""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return  user_info
# user_profile = build_profile('albert', 'einsten', location='princeton', field='physics')
# print(user_profile)

# def sandwich(*components):
#     print("Here we have sandwich with:")
#     for component in components:
#         print(f"- {component}")
# sandwich("beef", "cheese", "mushrooms")

# def build_profile(first, last, **user_info):
#     """Строит словарь с информацией о пользователе"""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return  user_info
# user_profile = build_profile('kirill',
#                              'tarasov',
#                              english = 'B2',
#                              education = 'higher',
#                              favourite_program = 'python',
#                              sport = 'CMS'
#                              )
# print(user_profile)

# def make_car(producer, model, **car_info):
#     """Строит словарь с информацией об автомобиле"""
#     car_info['producer'] = producer
#     car_info['model'] = model
#     return  car_info
# car = make_car('subaru',
#                'outback',
#                color = 'blue',
#                tow_package = True
#                )
# print(car)

# import functions
# functions.make_pizza(16, 'pepperoni')
# functions.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# from functions import make_pizza
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# from functions import make_pizza as mp
# mp(16, 'pepperoni', 'extra cheese')

# import functions as f
# f.make_pizza(16, 'cheese')

# from functions import *
# make_pizza(22, 'cheese')

# import  functions
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# # [:] создает копию
# functions.print_models(unprinted_designs, completed_models)
# functions.show_completed_models(completed_models)


# глава 9
# class Dog():
#     """Простая модель собаки."""
#
#     def __init__(self, name, age):
#         """Ининциализирует атрибуты name и age"""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """Собака садится по команде"""
#         print(f"{self.name.title()} is now sitting.")
#
#     def roll_over(self):
#         """Собака перекатывается по команде"""
#         print(f"{self.name.title()} rolled over!")
#
# my_dog = Dog('willie', 6)
# your_dog = Dog('lucy', 3)
# print(f"My dog's name is {my_dog.name.title()}")
# print(f"My dog is {my_dog.age} years old")
# my_dog.sit()
# print(f"\nYour dog's name is {your_dog.name.title()}.")
# print(f"Your dog is {your_dog.age} years old.")
# your_dog.roll_over()

# class Restaurant():
#     """Простая модель ресторана."""
#
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print(f"{self.restaurant_name.title()} {self.cuisine_type} restaurant"
#               f" is waiting for you!")
#
#     def open_restaurant(self):
#         print("Restaurant is open.")
#
#
# frenchRestaurant = Restaurant("claude monet", "french")
# chineseRestaurant = Restaurant("shi fu", 'chinese')
# koreanRestaurant = Restaurant("ta shi", 'korean')
# frenchRestaurant.describe_restaurant()
# chineseRestaurant.describe_restaurant()
# koreanRestaurant.describe_restaurant()

# class User():
#     """Простая модель пользователя"""
#
#     def __init__(self,
#                  first_name,
#                  last_name,
#                  age,
#                  location):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.location = location
#
#     def describe_user(self):
#         full_name = f"{self.first_name.title()} {self.last_name.title()}"
#         print(f"Information about user:"
#               f"\n\tname: {full_name}"
#               f"\n\tage: {self.age}"
#               f"\n\tlocation: {self.location.title()}")
#
#     def greet_user(self):
#         print(f"Hello, {self.first_name.title()} {self.last_name.title()}")
#
# tarasqua = User('kirill', 'tarasov', 21, 'moscow')
# tarasqua.describe_user()
# tarasqua.greet_user()

# class Car():
#     """Простая модель автомобиля"""
#
#     def __init__(self, make, model, year=2010):
#         """Инициализирует атрибуты описания автомобиля"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#
#     def get_descriptive_name(self):
#         """Инициализирует аккуратно отформатированное описание"""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
#
#     def read_odometer(self):
#         """Выводит пробег машины в милях"""
#         print(f"This car has {self.odometer_reading} miles on it")
#
#     def update_odometer(self, mileage):
#         """
#         Устанавливает заданное значение на одометре
#         При попытке обратной подкрутки изменение отклоняется
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         """Увеличивает показания одометра с заданным приращением"""
#         self.odometer_reading += miles
#
# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()
# my_new_car.update_odometer(15)
# my_used_car = Car('subaru', 'outback', 2015)
# print(my_used_car.get_descriptive_name())
# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()

# class Restaurant():
#     """Простая модель ресторана."""
#
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print(f"{self.restaurant_name.title()} {self.cuisine_type} restaurant"
#               f" is waiting for you!")
#
#     def open_restaurant(self):
#         print("Restaurant is open.")
#
#     def set_number_served(self, visitors_number):
#         self.number_served = visitors_number
#
#     def increment_number_served(self, increment):
#         self.number_served += increment
#
#
# restaurant = Restaurant("Claude Monet", "french")
# restaurant.increment_number_served(10)
# print(restaurant.number_served)

# class User():
#     """Простая модель пользователя"""
#
#     def __init__(self,
#                  first_name,
#                  last_name,
#                  age,
#                  location):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.location = location
#         self.login_attempts = 0
#
#     def describe_user(self):
#         full_name = f"{self.first_name.title()} {self.last_name.title()}"
#         print(f"Information about user:"
#               f"\n\tname: {full_name}"
#               f"\n\tage: {self.age}"
#               f"\n\tlocation: {self.location.title()}")
#
#     def greet_user(self):
#         print(f"Hello, {self.first_name.title()} {self.last_name.title()}")
#
#     def increment_login_attempts(self):
#         self.login_attempts += 1
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#
#
# tarasqua = User('kirill', 'tarasov', 21, 'moscow')
# tarasqua.increment_login_attempts()
# tarasqua.increment_login_attempts()
# print(tarasqua.login_attempts)
# tarasqua.reset_login_attempts()
# print(tarasqua.login_attempts)

# class Car():
#     """Простая модель автомобиля"""
#
#     def __init__(self, make, model, year=2010):
#         """Инициализирует атрибуты описания автомобиля"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#         self.gas_tank = 20
#
#     def get_descriptive_name(self):
#         """Инициализирует аккуратно отформатированное описание"""
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
#
#     def read_odometer(self):
#         """Выводит пробег машины в милях"""
#         print(f"This car has {self.odometer_reading} miles on it")
#
#     def update_odometer(self, mileage):
#         """
#         Устанавливает заданное значение на одометре
#         При попытке обратной подкрутки изменение отклоняется
#         """
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self, miles):
#         """Увеличивает показания одометра с заданным приращением"""
#         self.odometer_reading += miles
#
#     def fill_gas_tank(self):
#         print(f"Tank is {self.gas_tank}")
#
#
# class Battery():
#     """Простая модель аккумулятора автомобиля"""
#
#     def __init__(self, battery_size=75):
#         """Инициализирует атрибуты аккумулятора"""
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         """Выводит информацию о мощности аккумулятора"""
#         print(f"This car has a {self.battery_size}-kWh battery.")
#
#     def get_range(self):
#         """Выводит приблизительный запас хода для аккумулятора."""
#         if self.battery_size == 75:
#             range = 260
#         elif self.battery_size == 100:
#             range = 315
#         print(f"This car can go about {range} miles on a full charge")
#
#     def upgrade_battery(self):
#         if self.battery_size != 100:
#             self.battery_size = 100
#
#
# class ElectricCar(Car):
#     """Представляет аспекты машины, специфические для электромобилей."""
#
#     def __init__(self, make, model, year):
#         """
#         Ининциализирует атрибуты дочернего класса
#         Затем инициализирует атрибуты, специфические для электромобиля
#         """
#         super().__init__(make, model, year)
#         self.battery_size = 75
#         self.battery = Battery()
#
#     def fill_gas_tank(self):
#         """У электромобилей нет бензобака"""
#         print("This car doesn't have a gas tank!")
#
#
# my_tesla = ElectricCar('tesla', 'model s', 2019)
# my_tesla.battery.get_range()
# my_tesla.battery.upgrade_battery()
# my_tesla.battery.get_range()

# from classes import Restaurant
# from dependent_classes import IceCreamStand as Ics
# restaurant = Restaurant("Chimichangi", "Chinese")
# restaurant.describe_restaurant()
# ice_cream = Ics('Willy wonka', 'Italian')
# ice_cream.input_flavor()
# ice_cream.output_flavors()

# from dependent_classes import Admin, Privileges
# user = Admin('Kirill', 'Tarasov', 21, 'Moscow')
# user.privileges.show_privileges()

# from classes import Car
# from dependent_classes import ElectricCar as EC
# my_beetle = Car('volkswagen', 'beetle', 2019)
# print(my_beetle.get_descriptive_name())
# my_tesla = EC('tesla', 'roadster', 2019)
# print(my_tesla.get_descriptive_name())

# from random import randint
# print(randint(1, 6))
#
# from random import choice
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# first_up = choice(players)
# print(first_up)

# from classes import Die
# six_sides = Die(6)
# ten_sides = Die(10)
# twenty_sides = Die(20)
# for r in range(1, 11):
#     twenty_sides.roll_die()

# from random import randint, choice
# casino = [50, 15]
# figures = ['d', 'w']
# casino.extend(figures)
# victory = ""
# my_ticket = "www15"
# count = 1
# while True:
#     for i in range(1, 5):
#         victory = f"{victory}{choice(casino)}"
#     if victory == my_ticket:
#         break
#     else:
#         victory = ""
#     count += 1
# print(count)

# Глава 10
# with open('D:\\pi.txt') as file_object:
#     contents = file_object.read()
# print(contents.rstrip())

# filename = "D:\\pi.txt"
# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())

# filename = "D:\\pi.txt"
# with open(filename) as file_object:
#     lines = file_object.readlines()
# for line in lines:
#     print(line.rstrip())

# filename = "D:\\pi.txt"
# with open(filename) as file_object:
#     lines = file_object.readlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
# print(f"{pi_string[:52]}...")
# print(len(pi_string))

# filename = "D:\\pi.txt"
# with open(filename) as file_object:
#     lines = file_object.readlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
# birthday = input("Enter your birthday, in the form mmddyy: ")
# if birthday in pi_string:
#     print("Your birthday appears in the first million digits of pi!")
# else:
#     print("Your birthday does not appear in the first million digits of pi.")
# print(pi_string.find(birthday))

# with open("learning_python.txt") as file_object:
#     contents = file_object.read()
# print(contents, "\n")
# with open("learning_python.txt") as file_object:
#     for line in file_object:
#         print(line.strip())
# print("")
# with open("learning_python.txt") as file_object:
#     lines = file_object.readlines()
# for line in lines:
#     print(line.strip())

# with open("learning_python.txt") as file_object:
#     contents = file_object.read().replace("Python", "C")
# print(contents, "\n")
#
# with open("learning_python.txt") as file_object:
#     lines = file_object.readlines()
# for line in lines:
#     print(line.replace("Python", "C").strip())

# with open("learning_python.txt", 'w') as file_object:
#     file_object.write("I love programming!\n")
#     file_object.write("I love creating new games.")

# with open("learning_python.txt", 'a') as file_object:
#     file_object.write("I also love finding meaning in large datasets.\n")

# def guest(count, name):
#     with open("guests.txt", 'a') as file_object:
#         file_object.write(f"{count}. {name}\n")
#
#
# count = 1
# while True:
#     name = input("Input your name: ")
#     if name != "":
#         guest(count, name.title())
#         count += count
#     else:
#         break

# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
#
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number)/int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by 0!")
#     else:
#         print(answer)

# filename = "alice.txt"
# try:
#     with open(filename, encoding='utf-8') as f:
#         contents = f.read()
# except FileNotFoundError:
#     print(f"Sorry, the file {filename} doesn't exist.")

# from functions import count_words
# filenames = ['D:\\alice.txt', 'moby_dick']
# for filename in filenames:
#     count_words(filename)

# from functions import sum_numbers
# while True:
#     answer = input("Хотите сложить пару чисел? ")
#     if answer == 'нет':
#         break
#     elif answer == 'да':
#         sum_numbers()
#     else:
#         print("Введите 'да' или 'нет'")

# from functions import try_read
# filinames = ['cas.txt', 'dogs.txt']
# for filiname in filinames:
#     try_read(filiname)

# from functions import try_count_the
# try_count_the('D:\\alice.txt')

# import json
# numbers = [2, 3, 5, 7, 11, 13]
# filemane = 'numbers.json'
# with open(filemane, 'w') as f:
#     json.dump(numbers, f)
# with open(filemane) as f:
#     numbers_new = json.load(f)
# print(numbers_new)

# import json
# username = input("What is your name? ")
# filename = 'username.json'
# with open(filename, 'w') as f:
#     json.dump(username.title(), f)
#     print(f"We'll remember you when you come back, {username.title()}")
# import json
# filename = 'username.json'
# with open(filename) as f:
#     username = json.load(f)
#     print(f"Welcome back, {username}!")

# import json
# favourite_number = input("Input your favourite number: ")
# with open("favourite_number.json", 'w') as f:
#     json.dump(favourite_number, f)
#
# with open("favourite_number.json") as f:
#     number = json.load(f)
#     print(f"I know your favourite number! It's {number}")


# from functions import greet_user
# filename = 'username.json'
# greet_user(filename)
