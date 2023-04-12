"""
принимает в качестве аргументов три натуральных числа, и возвращает
значение True если существует невырожденный треугольник со сторонами
side1, side2, side3 и False в противном случае.
"""

# def is_valid_triangle(side1, side2, side3):
#     return side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2
#
#
# a, b, c = int(input()), int(input()), int(input())
#
#
# # вызываем функцию
# print(is_valid_triangle(a, b, c))
#

"""
Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное 
число и возвращает значение True если число является простым и False в противном случае.
"""

# def is_prime(num):
#     return len([1 for i in range(1, num + 1) if num % i == 0]) == 2


# n = int(input())
#
#
# print(is_prime(n))

"""
Напишите функцию get_next_prime(num), которая принимает в качестве аргумента 
натуральное число num и возвращает первое простое число большее числа num
"""

# def get_next_prime(num):
#     num += 1
#     while not is_prime(num):
#         num += 1
#     return num
#
#
# n = int(input())
#
# print(get_next_prime(n))

"""
Напишите функцию is_password_good(password), которая принимает в качестве аргумента
строковое значение пароля password и возвращает значение True если пароль является 
надежным и False в противном случае.
"""

# def is_password_good(password):
# if len(password) < 8:
#     return False
# flag1 = False
# flag2 = False
# flag3 = False
# for c in password:
#     if c.isupper():
#         flag1 = True
#     elif c.islower():
#         flag2 = True
#     elif c.isdigit():
#         flag3 = True
# return flag1 and flag2 and flag3


#     if len(password) < 8:
#         return False
#     digit = upper = lower = False
#     for c in password:
#         digit |= c.isdigit()  # digit равно False или если есть цифра то True
#         upper |= c.isupper()
#         lower |= c.islower()
#     return digit & upper & lower
#
#
# txt = input()
#
# print(is_password_good(txt))

"""
Проверить, если строки отличаются только на один символ
"""


# def is_one_away(word1, word2):
#     if len(word1) != len(word2):
#         return False
#     count = 0
#     for i in range(len(word1)):
#         if word1[i] != word2[i]:
#             count += 1
#     return count == 1
#
#
# txt1 = input()
# txt2 = input()
#
# print(is_one_away(txt1, txt2))

"""

"""


# def is_palindrome(text):
#     text1 = []
#     for i in text:
#         if i not in " ,-.?!№#$":
#             text1.append(i.lower())
#
#     return text1 == text1[::-1]
#
#
# txt = input()
#
# print(is_palindrome(txt))


# def is_palindrome(num):
#     return num == num[::-1]
#
#
# def is_prime(num):
#     return len([1 for i in range(1, num + 1) if num % i == 0]) == 2
#
#
# def is_even(num):
#     return num % 2 == 0
#
#
# def is_valid_password(password):
#     if password.count(":") != 2:
#         return False
#     a, b, c = password.split(":")[0], password.split(":")[1], password.split(":")[2]
#     return is_palindrome(a) + is_prime(int(b)) + is_even(int(c)) == 3
#
#
# psw = input()
#
#
# print(is_valid_password(psw))


# def is_correct_bracket(text):
#     while "()" in text:
#         text = text.replace('()', '')
#     return text == ''
#
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_correct_bracket(txt))


def convert_to_python_case(text):
    return ''.join(['_'+c.lower() if c.isupper() else c for c in text]).lstrip('_')


txt = input()

print(convert_to_python_case(txt))

