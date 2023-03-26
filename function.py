# def draw_box():
#     print('*' * 10)
#     for _ in range(12):
#         print('*' + ' ' * 8 + '*')
#     print('*' * 10)
#
#
# draw_box()
#

# def draw_triangle():
#     for i in range(1, 11):
#         print('*' * i)
#
#
# draw_triangle()

# def print_text(text, num):
#     while num > 0:
#         print(text, end='')
#         num -= 1
#
#
# print_text('Python', 4)


# def draw_triangle(fill, base):
#     for i in range(1, base // 2 + 2):
#         print(fill * i)
#     for i in range(base // 2, 0, -1):
#         print(fill * i)
#
#
# draw_triangle(input(), int(input()))


# def print_fio(name, surname, patronymic):
#     a = surname[0] + name[0] + patronymic[0]
#     print(a.upper())
#
#
# name, surname, patronymic = input(), input(), input()
#
# # вызываем функцию
# print_fio(name, surname, patronymic)

# def print_fio(name, surname, patronymic):
#     print((surname[0] + name[0] + patronymic[0]).upper())
#
#
# name, surname, patronymic = input(), input(), input()
#
# # вызываем функцию
# print_fio(name, surname, patronymic)


# def print_digit_sum(num):
#     print(sum(int(i) for i in str(num)))
#
#
# print_digit_sum(12345)


x = 5


# def add():
#     global x
#     x = 3
#     x = x + 5
#     print(x)
#
#
# add()
# print(x)  # ответ 8 и 8! Мы изменили х в функции!


# def get_sum(x, y, z):
#     return x + y + z
#     print('Сумма равна', x + y + z)  # после ретурн ничего не выполняется
#
#
# print(get_sum(1, 2, 3))


# def convert_to_miles(km):
#     return km * 0.6214
#
# # считываем данные
# num = int(input())
#
# # вызываем функцию
# print(convert_to_miles(num))


# def get_days(month):
#     if month in (1, 3, 5, 7, 8, 10, 12):
#         return 31
#     elif month in (4, 6, 9, 11):
#         return 30
#     else:
#         return 28
#
#
# num = int(input())
#
#
# print(get_days(num))


# def get_factors(num):
#     return [i for i in range(1, num // 2 + 1) if num % i == 0] + [num]
#
#
# n = int(input())
#
#
# print(get_factors(n))
#
#
# def number_of_factors(num):
#     return len(get_factors(num))
#
#
# n = int(input())
#
#
# print(number_of_factors(n))


# def find_all(target, symbol):
#     return [i for i in range(len(target)) if target[i] == symbol]
#     # return [index for index, i in enumerate(target) if i == symbol]
#
#
# s = input()
# char = input()
#
#
# print(find_all(s, char))
