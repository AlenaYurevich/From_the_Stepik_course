# n = int(input())
# my_list = []
# for i in range(1, n + 1):
#     my_list.append(i)
# print(my_list)


"""
Напишите программу, которая выводит список, состоящий из
n букв английского алфавита ['a', 'b', 'c', ...] в нижнем регистре
"""
# n = int(input())
# my_list = []
# for i in range(97, 97 + n):
#     my_list.append(chr(i))
# print(my_list)

"""
Дополните приведенный код, так чтобы он вывел сумму минимального и максимального элементов списка numbers
"""
# numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
# print(min(numbers) + max(numbers))

"""
Дополните приведенный код так, чтобы он вывел среднее арифметическое элементов списка evens
"""
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
average = sum(evens) / len(evens)
print(average)
