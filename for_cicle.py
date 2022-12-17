n = int(input('input number _ '))
for i in range(n + 1):
    print('*' * n)
    n -= 1


m, p, n = int(input('microorganisms_')), int(input('grown in percent_')), int(input('number of days_'))
for i in range(n):
    print(i + 1, m)
    m += m * p / 100

"""
На вход программе подаются два целых числа a и b (a≤b). Напишите программу, которая подсчитывает количество чисел в диапазоне от a до b включительно, куб которых оканчивается на 4 или 9.
"""
a, b = int(input()), int(input())
counter = 0
for i in range(a, b + 1):
    m = [4, 9]
    cube = i**3
    if cube % 10 in m:
        counter += 1
print(counter)


"""
На вход программе подается натуральное число n, а затем n целых чисел, каждое на отдельной строке. Напишите программу, которая подсчитывает сумму введенных чисел. 
"""
n = int(input())
total = 0
for _ in range(n):
    a = int(input())
    total += a
print(total)

