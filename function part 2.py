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


def is_password_good(password):
    counter = 0
    if len(password) > 7:
        counter += 1
    for i in password:
        if i.islower():
            counter += 1
            break
    for i in password:
        if i.isupper():
            counter += 1
            break
    for i in password:
        if i.isdigit():
            counter += 1
            break
    return counter == 4


txt = input()

print(is_password_good(txt))

#  посмотри форум решений
