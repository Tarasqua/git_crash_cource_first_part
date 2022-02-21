import unittest
from functions import get_formatted_name, city_country
from classes import AnonymousSurvey, Employee


# while True:
#     first = input("\nPlease, give me a first name: ")
#     if first == 'q':
#         break
#     last = input("Please, give me a last one: ")
#     if last == 'q':
#         break
#     formatted_name = get_formatted_name(first, last)
#     print(f"\n\tNeatly formatted name: {formatted_name}.")


# class NamesTestCase(unittest.TestCase):
#     """Тесты для 'get_formatted_name'"""
#
#     def test_first_last_name(self):
#         """Имена вида 'Janis Joplin' работают правильно?"""
#         formatted_name = get_formatted_name('janis', 'joplin')
#         self.assertEqual(formatted_name, 'Janis Joplin')
#
#     def test_first_last_middle_name(self):
#         """Работают ли такие имена, как 'Wolfgang Amadeus Mozart?"""
#         formatted_name = get_formatted_name(
#             'wolfgang', 'mozart', 'amadeus')
#         self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
#
#
# if __name__ == '__main__':
#     unittest.main()


# class CitiesTestCase(unittest.TestCase):
#     """Тесты для 'city_country'"""
#
#     def test_city_country(self):
#         """Названия вида 'Santiago, Chile' работают правильно?"""
#         formatted_city = city_country('santiago', 'chile')
#         self.assertEqual(formatted_city, 'Santiago, Chile')
#
#     def test_city_country_population(self):
#         """Название вида 'Santiago, Chile - population 5_000_000'"""
#         formatted_city = city_country('santiago', 'chile', 5_000_000)
#         self.assertEqual(formatted_city, 'Santiago, Chile - population 5000000')
#
#
# if __name__ == '__main__':
#     unittest.main()


# # Определение вопроса с созданием экземпляра AnonymousSurvey.
# question = "What language did you first learn to speak?"
# my_survey = AnonymousSurvey(question)
#
# # Вывод вопроса и сохранение ответов.
# my_survey.show_questions()
# print("Enter 'q' at any time to quit.\n")
# while True:
#     response = input("Language: ")
#     if response == 'q':
#         break
#     my_survey.store_response(response)
#
# # Вывод результатов опроса.
# print("\nThank you to everyone who participated in the survey!")
# my_survey.show_results()


# class TestAnonymousSurvey(unittest.TestCase):
#     """Тесты для класса AnonymousSurvey"""
#
#     def setUp(self):
#         """Создание опроса и набора ответов для всех тестовых методов."""
#         question = "What language did you first learn to speak?"
#         self.my_survey = AnonymousSurvey(question)
#         self.responses = ['English', 'Spanish', 'Mandarin']
#
#     def test_store_single_response(self):
#         """Проверяет, что один ответ сохранен правильно."""
#         self.my_survey.store_response(self.responses[0])
#         self.assertIn(self.responses[0], self.my_survey.responses)
#
#     def test_store_three_responses(self):
#         """Проверяет, что три ответа были сохранены правильно."""
#         for response in self.responses:
#             self.my_survey.store_response(response)
#         for response in self.responses:
#             self.assertIn(response, self.my_survey.responses)
#
#
# if __name__ == '__main__':
#     unittest.main()

class TestEmployee(unittest.TestCase):
    """Тесты для класса Employee"""

    def setUp(self):
        """Создание рабочего"""
        name = 'Igor'
        lastname = 'Kornelyuk'
        self.salary = 2000
        self.default_increase = 5000
        self.custom_increase = 8000
        self.my_employee = Employee(name, lastname, self.salary)

    def test_give_default_raise(self):
        self.my_employee.salary_raise()
        self.assertEqual(self.salary + self.default_increase, self.my_employee.salary)

    def test_give_custom_rise(self):
        self.my_employee.salary_raise(self.custom_increase)
        self.assertEqual(self.salary + self.custom_increase, self.my_employee.salary)


if __name__ == '__main__':
    unittest.main()