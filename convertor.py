#  число из шестнадцатиричной системы в десятичную

# n = input()
# print(int(n, 16))  # 16 - база


#  число из двоичной системы в десятичную

# n = input()
# print(int(n, 2))  # - база


# n = 9
# for i in range(18):
#     print(n, int('88', n) == int('32', n) + int('22', n) + int('16', n) + int('17', n))
#     n += 1


# n = int(input('Введите десятичное число:\n'))
# s = int(input('Введите систему счисления:\n'))
# res = []
# numbers = '0123456789ABCDEF'
# while n > 0:
#     res.append(n % s)
#     n = n // s
#
# l16 = []
# if s == 16:  # если шестнадцатеричная система
#     for i in res:
#         l16.append(numbers[i])
#     print(*l16[::-1], sep='')
# else:  # если любая другая система
#     print(*res[::-1], sep='')


num = 127

bin_num = bin(num)  # 0b1111111
oct_num = oct(num)  # 0o177
hex_num = hex(num)  # 0x7f

print(bin_num[2:])  # 1111111
print(oct_num[2:])  # 177
print(hex_num[2:])  # 7f


num = 127432

hex_num = hex(num)          # 0x1f1c8
print(hex_num[2:].upper())  # 1F1C8

#  десятичное число переводим в двоичную, восьмеричную и шестнадцатиричную систему счисления

num = int(input('Введите число  '))
bin_num = bin(num)
oct_num = oct(num)
hex_num = hex(num)

print(bin_num[2:])
print(oct_num[2:])
print(hex_num[2:].upper())
