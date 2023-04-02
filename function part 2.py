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


def is_prime(num):
    return 1 < len([1 for i in range(1, num + 1) if num % i == 0]) < 3


n = int(input())


print(is_prime(n))
