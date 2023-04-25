# def get_middle_point(x1, y1, x2, y2):
#     return (x1 + x2) / 2, (y1 + y2) / 2
#
#
# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())
#
#
# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)


# from math import pi
#
#
# def get_circle(radius):
#     return 2 * pi * radius, pi * radius ** 2
#
#
# r = float(input())
#
#
# print(get_circle(r))


# from math import sqrt
# def solve(a, b, c):
#     d = b ** 2 - 4 * a * c
#     x1, x2 = (-b + sqrt(d)) / (2 * a), (-b - sqrt(d)) / (2 * a)
#     return min(x1, x2), max(x1, x2)
#
#
# a, b, c = int(input()), int(input()), int(input())
#
#
# x1, x2 = solve(a, b, c)
# print(x1, x2)


# объявление функции
# def draw_triangle():
#     n = 16
#     for i in range(1, n, 2):
#         print(' ' * int((n - i) // 2) + '*' * i)
#
#
# # основная программа
# draw_triangle()  # вызов функции

# объявление функции
# def get_shipping_cost(quantity):
#     return 1000 + 120 * (quantity - 1)
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_shipping_cost(n))


# from math import factorial as f
#
#
# def compute_binom(n, k):
#     return f(n) // (f(k) * f(n - k))
#
#
# # считываем данные
# n = int(input())
# k = int(input())
#
# # вызываем функцию
# print(compute_binom(n, k))


# объявление функции
# def number_to_words(num):
#     tens = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать',
#             'семнадцать', 'восемнадцать', 'девятнадцать']
#     units = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
#     dec = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят',
#     'девяносто']
#     if num < 10:
#         return units[num]
#     elif num < 20:
#         return tens[num % 10]
#     elif num % 10 == 0:
#         return dec[num // 10]
#     else:
#         return dec[num // 10] + ' ' + units[num % 10]
#
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(number_to_words(n))


# def get_month(language, number):
#     en = ['', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
#           'november', 'december']
#     ru = ['', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь',
#           'ноябрь', 'декабрь']
#     return en[number] if language == "en" else ru[number]
#
#
# lan = input()
# num = int(input())
#
#
# print(get_month(lan, num))


# def is_magic(date):
#     num = date.split('.')
#     return int(num[0]) * int(num[1]) == int(num[2][2:])
#
#
# date = input()
#
#
# print(is_magic(date))


def is_pangram(text):
    pangram = text.replace(' ', '').lower()
    glif = 'abcdefghijklmnopqrstuvwxyz'
    for i in glif:
        if i not in pangram:
            return False
    return True


text = input()


print(is_pangram(text))
