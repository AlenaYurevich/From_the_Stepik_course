n = int(input('input number _ '))
for i in range(n + 1):
    print('*' * n)
    n -= 1


m, p, n = int(input('microorganisms_')), int(input('grown in percent_')), int(input('number of days_'))
for i in range(n):
    print(i + 1, m)
    m += m * p / 100
