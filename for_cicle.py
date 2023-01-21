# n = int(input('input number _ '))
# for i in range(n + 1):
#     print('*' * n)
#     n -= 1


# m, p, n = int(input('microorganisms_')), int(input('grown in percent_')), int(input('number of days_'))
# for i in range(n):
#     print(i + 1, m)
#     m += m * p / 100

"""
На вход программе подаются два целых числа
 a и b (a≤b). Напишите программу, которая подсчитывает количество чисел в диапазоне
 от a до b включительно, куб которых оканчивается на 4 или 9.
"""
# a, b = int(input()), int(input())
# counter = 0
# for i in range(a, b + 1):
#     m = [4, 9]
#     cube = i**3
#     if cube % 10 in m:
#         counter += 1
# print(counter)


"""
На вход программе подается натуральное число n, а затем n целых чисел, каждое на отдельной 
строке. Напишите программу, которая подсчитывает сумму введенных чисел. 
"""
# n = int(input())
# total = 0
# for _ in range(n):
#     a = int(input())
#     total += a
# print(total)

"""
factorial n
"""
# n = int(input())
# total = 1
# for i in range(2, n + 1):
#     total *= i
# print(total)

"""
multiplied sequence
"""
# total = 1
# for _ in range(10):
#     n = int(input())
#     if n != 0:
#         total *= n
# print(total)

"""
Sum of all divisors
"""
# total = 1
# n = int(input())
# for i in range(2, n + 1):
#     if n % i == 0:
#         total += i
# print(total)


"""
1−2+3−4+5−6+…+(−1) ** n+1 * n
"""
# total = 0
# for i in range(1, int(input()) + 1):
#     if i % 2 == 0:
#         total -= i
#     else:
#         total += i
# print(total)

"""
find two max number from sequence
"""
# mylist = []
# for _ in range(int(input())):
#     num = int(input())
#     mylist.append(num)
# mylist.sort()
# print(mylist[-1])
# print(mylist[-2])


"""
to find all numbers in sequence are even
"""
# flag = "YES"
# for _ in range(10):
#     num = int(input())
#     if num % 2 == 1:
#         flag = "NO"
#         break
# print(flag)


"""
number fibonacci
"""
# fib1 = 1
# fib2 = 1
# n = int(input())
# for _ in range(n):
#     print(fib1, end=" ")
#     fib1, fib2 = fib2, fib1 + fib2

"""
a clock
"""
# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             print(hours, ':', minutes, ':', seconds)

"""
printing
"""
# for i in range(8):
#     for j in range(i + 1):
#         print('*', end='')
#     print()


"""
Программа должна вывести таблицу размером n×5 в соответствии с условием.
"""
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(5):
#         print(i, end=' ')
#     print()


"""
Программа должна вывести таблицу сложения для всех чисел от 1 до n.
"""
# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, 10):
#         print(i, '+', j, '=', i + j)
#     print()

"""
Напишите программу, которая печатает равнобедренный звездный треугольник с основанием, равным n 
"""
# n = int(input())
# counter = n // 2 + 1
# for i in range(1, counter):
#     print('*' * i)
# for i in range(counter, 0, -1):
#     print('*' * i)


"""
Программа должна вывести треугольник в соответствии с условием
"""
# n = int(input())
# for i in range(1, n + 1):
#     print(str(i) * i)


"""
Корни квадратного уравнения
"""
# total = 0
# for x in range(1, 45):
#     for y in range(1, 45):
#         for z in range(1, 45):
#             if x ** 2 + y ** 2 + z ** 2 == 2020:
#                 total += 1
#                 print('x =', x, 'y =', y, 'z =', z)
# print('Общее количество натуральных решений =', total)

"""
Находим незвестные переменные в цикле
"""
# for n in range(13):
#     for k in range(12):
#         for m in range(12):
#             if 28 * n + 30 * k + 31 * m == 365:
#                 print('n =', n, 'k =', k, 'm =', m)

"""
Старинная задача
Имеется 100100 рублей. Сколько быков, коров и телят можно купить на все эти деньги,
 если плата за быка – 10 рублей, за корову – 5 рублей, за теленка – 0.5 рубля 
 и надо купить 100 голов скота?
"""
# for b in range(11):
#     for k in range(21):
#         for t in range(0, 99, 2):
#             if b * 10 + k * 5 + t * 0.5 == 100 and b + k + t == 100:
#                 print('b = ', b, 'k = ', k, 't = ', t)

"""
найдите четыре положительных целых числа, сумма 5-х степеней которых равна
5-й степени другого положительного целого числа.
"""
for a in range(75, 2, -1):
    for b in range(150, a, -1):
        for c in range(150, b, -1):
            for d in range(150, c, -1):
                for e in range(150, d, -1):
                    if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
                        print(a + b + c + d + e)
                        break
