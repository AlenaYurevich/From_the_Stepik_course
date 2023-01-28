# while True:
#     a = input()
#     if a == "КОНЕЦ":
#         break
#     print(a)


"""
На вход программе подается последовательность слов, каждое слово на отдельной строке.
Концом последовательности является слово «КОНЕЦ» или «конец» (большими или 
маленькими буквами, без кавычек). Напишите программу, которая выводит члены 
данной последовательности
"""
# while (text := input()) not in "КОНЕЦконец":
#     print(text)


"""
Концом последовательности является одно из трех слов: «стоп», «хватит», «достаточно» 
(маленькими буквами, без кавычек)
"""
# counter = 0
# while (text := input()) not in ('стоп', 'хватит', 'достаточно'):
#     counter += 1
# print(counter)

"""
Концом последовательности является любое число не делящееся на 7
"""
# while True:
#     num = int(input())
#     if num % 7 != 0:
#         break
#     print(num)

# num = int(input())
# has_seven = False  # сигнальная метка
#
# while num != 0:
#     last_digit = num % 10
#     if last_digit == 7:
#         has_seven = True
#     num = num // 10
#
# if has_seven:
#     print('YES')
# else:
#     print('NO')

"""
Программа должна вывести цифры введенного числа в столбик в обратном порядке
"""
# num = int(input())
# while num != 0:
#     print(num % 10)
#     num = num // 10


"""
Программа должна вывести число, записанное в обратном порядке
"""
# num = int(input())
# while num != 0:
#     print(num % 10, end='')
#     num = num // 10

"""
Программа должна вывести максимальную и минимальную цифры введенного числа
"""
# max_num = 0
# min_num = 10
# num = int(input())
# while num:
#     if num % 10 > max_num:
#         max_num = num % 10
#     if num % 10 < min_num:
#         min_num = num % 10
#     num = num // 10
# print("Максимальная цифра равна", max_num)
# print("Минимальная цифра равна", min_num)

"""
Дано натуральное число. Программа, которая вычисляет:
сумму его цифр;
количество цифр в нем;
произведение его цифр;
среднее арифметическое его цифр;
его первую цифру;
сумму его первой и последней цифры.
"""
# num = int(input())
# num_multiply = 1
# digits = []
# while num:
#     digit = num % 10
#     digits.append(digit)
#     num_multiply *= digit
#     num = num // 10
# num_total = sum(digits)
# num_len = len(digits)
# num_average = num_total / num_len
# print(num_total, num_len, num_multiply, num_average, digits[-1], digits[-1] + digits[0], sep='\n')

"""
Напишите программу, которая определяет вторую (с начала) цифру.
"""
# num = str(input())
# print(num[1])

"""
Цифровой корень числа n получается следующим образом:
если сложить все цифры этого числа, затем все цифры найденной суммы
и повторить этот процесс, то в результате будет получено 
однозначное число (цифра), которое и называется цифровым корнем данного числа.
"""
# n = int(input())
# while n > 9:
#     n = n // 10 + n % 10
# print(n)


"""
Сумма факториалов от числа n до 1
"""
# n = int(input())
# total = 1
# for i in range(2, n + 1):
#     factorial = 1
#     while i > 1:
#         factorial *= i
#         i -= 1
#     total += factorial
# print(total)


"""
if number is prime
"""
a, b = int(input()), int(input())
for n in range(a, b + 1):
    prime = True
    i = 2
    while i < n and prime:
        if n % i == 0:
            prime = False
        i += 1
    if n != 1 and prime:
        print(n)
