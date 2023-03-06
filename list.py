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
# evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# average = sum(evens) / len(evens)
# print(average)


# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
# rainbow[3] = 'Зеленый'
# print(rainbow)


# languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali',
# 'Portuguese', 'Russian', 'Japanese', 'Lahnda']
# print(languages[::-1])


# numbers1 = [1, 2, 3]
# numbers2 = [6]
# numbers3 = [7, 8, 9, 10, 11, 12, 13]
# print(numbers1 * 2 + numbers2 * 9 + numbers3)


"""
Что будет выведено в результате выполнения следующего программного кода
"""
# numbers = [4, 2]
# numbers.extend([1, 2, 3])
# numbers.extend([7, 17, 777])
# print(numbers)

"""

"""
# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'brown', 'magenta']
# del colors[2]
# del colors[6]
# print(colors)

"""
Дополните приведенный код, чтобы он:
Вывел длину списка;
Вывел последний элемент списка;
Вывел список в обратном порядке (вспоминаем срезы);
Вывел YES если список содержит числа 5 и 17, и NO в противном случае;
Вывел список с удаленным первым и последним элементами.
"""
# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5,
# 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# print(len(numbers))
# print(numbers[-1])
# print(numbers[::-1])
# print('YES' if 5 in numbers and 17 in numbers else 'NO')
# print(numbers[1:-1])

"""
На вход программе подается натуральное число n, а затем n строк. Напишите программу,
которая создает из указанных строк список и выводит его
"""
# n = int(input())
# my_list = []
# for i in range(n):
#     my_list.append(input())
# print(my_list)


"""
Напишите программу, выводящую следующий список
"""
# n = 1
# funlist = []
# for i in range(97, 123):
#     funlist.append(chr(i) * n)
#     n += 1
# print(funlist)
#
# a = []
# for i in range(1, 27):
#     a.append(chr(96 + i) * i)
# print(a)


"""
На вход программе подаются натуральное число n, а затем n целых чисел, каждое на отдельной строке.
"""
# a = []
# for i in range(int(input())):
#     a.append(int(input()) ** 3)
# print(a)


"""
Программа должна вывести список, состоящий из делителей введенного числа
"""
# a = [1]
# n = int(input())
# for i in range(2, int(n / 2 + 1)):  # проверяем до половины числа
#     if n % i == 0:
#         a.append(i)
# a.append(n)  # последним добавляем само число
# print(a)


"""
Программа должна вывести список, состоящий из сумм соседних чисел
"""
# n = int(input())
# a = []
# b = []
# for i in range(n):
#     a.append(int(input()))
# for j in range(1, n):
#     b.append(a[j] + a[j - 1])
# print(b)


"""
На вход программе подается натуральное число n, а затем n целых чисел. Напишите
 программу, которая создает из указанных чисел список, затем удаляет все элементы
  стоящие по нечетным индексам, а затем выводит полученный список
"""
# a = []
# for i in range(int(input())):
#     a.append(int(input()))
# del a[1::2]
# print(a)


"""
На вход программе подается натуральное число n и n строк, а затем число k. Напишите 
программу, которая выводит k-ую букву из введенных строк на одной строке без пробелов
"""
# n = int(input())
# my_list = [input() for _ in range(n)]
# k = int(input())
# for i in range(n):
#     if len(my_list[i]) >= k:
#         print(my_list[i][k - 1], end='')


"""
Программа должна вывести список состоящий из символов всех введенных строк
"""
# a = []
# for i in range(int(input())):
#     a.extend(input())
# print(a)

"""
Распаковка списка через *
"""
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(*numbers, sep='\n')


"""
Дополните приведенный код, так чтобы он вывел сумму квадратов элементов списка numbers
"""
# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# print(sum(num ** 2 for num in numbers))

"""
Программа должна вывести сначала введенные числа, затем пустую строку, а затем соответствующие значения функции
"""
# n = int(input())
# a = []
# b = []
# for i in range(n):
#     x = int(input())
#     a.append(x)
#     b.append(x ** 2 + 2 * x + 1)
# print(*a, sep='\n')
# print()
# print(*b, sep='\n')


"""
Напишите программу, которая удаляет наименьшее и наибольшее значение из
указанных чисел, а затем выводит оставшиеся числа каждое на отдельной строке, не меняя их порядок
"""
# n = int(input())
# a = []
# for i in range(n):
#     x = int(input())
#     a.append(x)
# a.remove(min(a))
# a.remove(max(a))
# print(*a, sep='\n')

"""
На вход программе подается натуральное число n, а затем n строк. Напишите программу, 
которая выводит только уникальные строки, в том же порядке, в котором они были введены
"""
# n = int(input())
# a = []
# for i in range(n):
#     x = input()
#     if x not in a:
#         a.append(x)
# print(*a, sep='\n')


"""
Напишите программу, которая выводит все введенные строки, в которых встречается поисковый запрос
"""
# n = int(input())
# a = []
# for i in range(n):
#     a.append(input())
# q = input().lower()
# for s in a:
#     if q in s.lower():
#         print(s)


"""
Напишите программу, которая выводит все введенные строки, в которых встречаются все поисковые запросы.
"""
# a, b = [], []
# for i in range(int(input())):
#     a.append(input())
# for j in range(int(input())):
#     b.append(input().lower())
# for fun_str in a:
#     for question in b:
#         if question not in fun_str.lower():
#             break
#     else:
#         print(fun_str)


"""
Напишите программу, которая сначала выводит все отрицательные числа, 
затем нули, а затем все положительные числа, каждое на отдельной строке.
Числа должны быть выведены в том же порядке, в котором они были введены.
"""
# numbers = [int(input()) for i in range(int(input()))]
# negatives, zero, positives = [], [], []
# for i in numbers:
#     if i < 0:
#         negatives.append(i)
#     if i == 0:
#         zero.append(i)
#     if i > 0:
#         positives.append(i)
# print(*negatives, *zero, *positives, sep='\n')


"""
Напишите программу, которая выводит слова введенной строки в столбик.
"""
# print(*input().split(), sep='\n')


"""
На вход программе подается строка текста, содержащая имя, отчество и фамилию человека.
Напишите программу, которая выводит инициалы человека
"""
# s = input().split()
# for i in s:
#     print(i[0], end='.')


"""
Напишите программу, которая разбирает строку на части, разделенные символом "\".
"""
# s = input()
# li = s.split('\\')
# for i in li:
#     print(i)


"""
На вход программе подается строка текста, содержащая целые числа.
Напишите программу, которая по заданным числам строит столбчатую диаграмму
"""
# s = input().split()
# for i in s:
#     print('+' * int(i))


"""
Программа должна вывести «ДА», если введеная строка является корректным 
ip-адресом, и «НЕТ» — в противном случае.
"""
# s = input().split('.')
# flag = 'ДА'
# for i in s:
#     if int(i) > 256:
#         flag = "НЕТ"
# print(flag)


"""
На вход программе подается строка текста и строка разделитель. 
Напишите программу, которая вставляет указанный разделитель между каждым символом введенной строки текста
"""
# s = input()
# sep = input()
# print(*s, sep=sep)


"""
*****На вход программе подается строка текста, содержащая натуральные числа. 
Из данной строки формируется список чисел. Напишите программу,
которая подсчитывает, сколько в полученном списке пар элементов, равных друг другу
"""
# s = input().split()
# counter = 0
# for i in s:
#     n = s.count(i) - 1
#     counter += n
#     s = s[1:]
# print(counter)
#
# sp = input().split()
# n = 0
# for i in range(len(sp)):
#     for j in range(i+1, len(sp)):
#         if sp[j] == sp[i]:
#             n += 1
# print(n)

"""
List methods
"""
# numbers = [8, 9, 10, 11]
# numbers[1] = 17
# numbers.extend([4, 5, 6])
# del numbers[0]
# numbers *= 2
# numbers.insert(3, 25)
# print(numbers)


"""
Из данной строки формируется список чисел. Напишите программу,
которая меняет местами минимальный и максимальный элемент этого списка.
"""
# s = input().split()
# li = [int(i) for i in s]
# min_ind = li.index(min(li))
# max_ind = li.index(max(li))
# li[min_ind], li[max_ind] = max(li), min(li)
# print(*li, sep=' ')


