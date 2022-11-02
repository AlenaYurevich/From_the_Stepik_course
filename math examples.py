from math import pi, sqrt

R = float(input())
print(pi * R ** 2)  # площадь круга
print(2 * pi * R)  # длина окружности

a, b = float(input()), float(input())
print((a + b) / 2)  # Среднее арифметическое
print(sqrt(a * b))  # Среднее геометрическое
print(2 * a * b / (a + b))  # Среднее гармоническое
print(sqrt((a ** 2 + b ** 2) / 2))  # Среднее квадратичное
