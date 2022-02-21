import math
import functools
import string
#
#
# # Задание №1.
# less_of_two_evens = lambda a, b: f"{a} less than {b}" if a < b \
#     else (f"{b} less than {a}" if b < a else f"{a} equals {b}")
# # Проверка.
# print(less_of_two_evens(2, 4))
# print(less_of_two_evens(25, 8))
# print(less_of_two_evens(16, 16))
#
#
# # Задание №2.
# animal_crackers = lambda str: True if list(str.split()[0])[0] == list(str.split()[1])[0] else False
# # Проверка.
# print(animal_crackers('Levelheaded Llama'))
# print(animal_crackers('Crazy Kangaroo'))
#
#
# # Задание №3.
# makes_twenty = lambda a, b: True if (a + b == 20 or a == 20 or b == 20) else False
# # Проверка.
# print(makes_twenty(20, 10))
# print(makes_twenty(12, 8))
# print(makes_twenty(2, 3))
#
#
# # Задание №4.
# def old_macdonald(name):
#     str = list(name)
#     for i in range(len(str)):
#         if i == 0 or i == 3:
#             str[i] = str[i].capitalize()
#     return "".join(str)
#
#
# # Проверка.
# print(old_macdonald('macdonald'))
#
#
# # Задание №5.
# master_yoda = lambda text: " ".join(reversed(text.split()))
# # Проверка.
# print(master_yoda('I am home'))
# print(master_yoda('We are ready'))
#
#
# # Задание №6.
# def almost_there(n):
#     return abs(100-n) <= 10 or abs(200-n) <= 10
#
#
# # Проверка.
# print(almost_there(104))
# print(almost_there(150))
# print(almost_there(209))
#
#
# # Задание №7.
# has_33 = lambda nums: print(True if str(nums).count('3, 3') else False)
# # Проверка
# has_33([1, 3, 3])
# has_33([1, 3, 1, 3])
# has_33([3, 1, 3])
#
#
# # Задание №8.
# paper_doll = lambda text: print(''.join([l*3 for l in list(text)]))
# # Проверка.
# paper_doll('Hello')
# paper_doll('Mississippi')
#
#
# # Задание №9.
# def blackjack(a, b, c):
#     s = a + b + c
#     if s <= 21:
#         return s
#     if s > 21:
#         if str([a, b, c]).count('11'):
#             return s - 10
#         else:
#             return 'BUST'
#
#
# # Проверка.
# print(blackjack(5, 6, 7))
# print(blackjack(9, 9, 9))
# print(blackjack(9, 9, 11))
#
#
# # Задание №10.
# def summer_69(arr):
#     section_depth = 0
#     total = 0
#     for num in arr:
#         if num == 6:
#             section_depth += 1
#         elif section_depth == 0:
#             total += num
#         elif num == 9 and section_depth > 0:
#             section_depth -= 1
#     return total
#
#
# # Проверка
# print(summer_69([1, 3, 5]))
# print(summer_69([4, 5, 6, 7, 8, 9]))
# print(summer_69([2, 1, 6, 9, 11]))
#
#
# # Задание №11.
# def spy_game(nums):
#     flag = 0
#     for i in nums:
#         if i == 0:
#             flag = flag + 1
#             continue
#         if flag >= 2 and i == 7:
#             return True
#     return False
#
#
# print(spy_game([1, 0, 4, 0, 0, 7, 5]))
# print(spy_game([1, 0, 2, 4, 0, 5, 7]))
# print(spy_game([1, 7, 2, 0, 4, 5, 0]))
#
#
# # Задание №12.
# def count_primes(num):
#     counter = 0
#     for n in range(2, num + 1):
#         prime = True
#         for i in range(2, n):
#             if n % i == 0:
#                 prime = False
#                 break
#         if prime:
#             counter += 1
#     return counter
#
#
# # Проверка
# print(count_primes(100))
#
#
# # Задание №13.
# def print_big(letter):
#     if letter.lower() == 'a':
#         return '  *\n * *\n*****\n*   *\n*   *'
#     elif letter.lower() == 'b':
#         return '*****\n*   *\n****\n*   *\n*****'
#     elif letter.lower() == 'c':
#         return ' ****\n*\n*\n*\n ****'
#     elif letter.lower() == 'd':
#         return '****\n*   *\n*   *\n*   *\n****'
#     elif letter.lower() == 'e':
#         return '*****\n*    \n****\n*    \n*****'
#
#
# arr = ['a', 'b', 'c', 'd', 'e']
# for i in arr:
#     print(print_big(i))
#
#
# # Задание #14.
# vol = lambda rad: float(4 / 3) * math.pi * (rad ** 3)
# # Проверка.
# print(round(vol(2), 2))
#
#
# # Задание №15.
# def ran_bool(num, low, high):
#     while low <= num < high:
#         return True
#     return False
#
#
# print(ran_bool(5, 2, 7))
# print(ran_bool(5, 2, 4))
#
#
# # Задание №15.
# def up_low(s):
#     count_up = 0
#     count_low = 0
#     for i in list(s):
#         if i.isupper():
#             count_up += 1
#         elif i.islower():
#             count_low += 1
#     if count_low == 0:
#         print(f"There are no lower case characters, but {count_up} upper ones")
#     elif count_up == 0:
#         print(f"There are no upper case letters, but {count_up} lower ones")
#     else:
#         print(f"There are {count_up} upper case letters, and {count_low} lower ones.")
#
#
# s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
# up_low(s)
#
#
# # Задание №16.
# def unique_list(lst):
#     temp = []
#     for x in lst:
#         if x not in temp:
#             temp.append(x)
#     return temp
#
#
# old_list = [1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]
# new_list = unique_list(old_list)
# print(f"First way: {new_list}")
# # Или проще
# print(f"Second way: {list(set(old_list))}")
#
#
# # Задание №17.
# def multiply(numbers):
#     m = 1
#     for n in numbers:
#         m *= n
#     return m
#
#
# # Проверка.
# print(f"First way: {multiply([1, 2, 3, -4])}")
# print(f"Second way: {functools.reduce(lambda a, b: a * b, [1, 2, 3, -4])}")
#
#
# # Задание №18.
# palindrome = lambda s: True if s == s[::-1] else False
# # Проверка.
# print(palindrome('helleh'))
#
#
# Задание №19.
def is_pangram(text):
    """
    Функция вычитает из множества всех букв множество букв, заданной строки и,
    если получает пустое множество, значит, в строке используются все буквы
    """
    if set(string.ascii_lowercase) - set(text.lower()) == set([]):
        return True
    else:
        return False


print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("Hi how are you"))

# Или через lambda
is_pangram_lambda = lambda text: True if set(string.ascii_lowercase) - set(text.lower()) == set([]) else False
print(is_pangram_lambda("The quick brown fox jumps over the lazy dog"))