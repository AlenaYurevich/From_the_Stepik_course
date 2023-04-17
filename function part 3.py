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


from math import sqrt
def solve(a, b, c):
    d = b ** 2 - 4 * a * c
    x1, x2 = (-b + sqrt(d)) / (2 * a), (-b - sqrt(d)) / (2 * a)
    return min(x1, x2), max(x1, x2)


a, b, c = int(input()), int(input()), int(input())


x1, x2 = solve(a, b, c)
print(x1, x2)
