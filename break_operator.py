"""
Программа должна вывести наименьший делитель отличный от 1
"""
# num = int(input())
# for i in range(2, num + 1):
#     if num % i == 0:
#         break
# print(i)


"""
Напишите программу, которая выводит числа от 1 до n включительно за исключением промежутков
"""
# num = int(input())
# for i in range(1, num + 1):
#     if i in range(5, 10) or i in range(17, 38) or i in range(78, 88):
#         continue
#     print(i)


"""
Сумма четных чисел от 0 до 1000
"""
# total = 0
# for i in range(2, 1001, 2):
#     total += i
# print(total)


"""
Упражнение на ревью кода
"""
# max_x = -10**6
# s = 0
# for _ in range(10):
#     x = int(input())
#     if x < 0:
#         s += x
#         if x > max_x:
#             max_x = x
# if s < 0:
#     print(s)
#     print(max_x)
# else:
#     print("NO")


"""
Упражнение на ревью кода
"""
# n = int(input())
# max_digit = -1
# if n == 0:
#     print(n)
# else:
#     while n > 0:
#         digit = n % 10
#         if digit % 3 == 0:
#             if digit > max_digit:
#                 max_digit = digit
#         n = n // 10
#     if max_digit == -1:
#         print('NO')
#     else:
#         print(max_digit)

"""
Упражнение на ревью кода
"""
n = int(input())
max_digit = 0
while n > 0:
    max_digit = n % 10
    n = n // 10
print(max_digit)
