# n = 7
# count = 0
# maximum = -10 ** 12
# for i in range(1, n + 2):
#     x = int(input())
#     if x % 4 == 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')


# n = 4
# count = 0
# maximum = -10 ** 8
# for i in range(n):
#     x = int(input())
#     if x % 2 != 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

# n = int(input())
# print('*' * 19)
# for _ in range(n - 2):
#     print('*', ' ' * 15, '*')
# print('*' * 19)

# n = int(input())
# count_of_3 = 0
# count_of_last_digit = 0
# my_last_digit = n % 10
# even = 0
# sum_of_num_more_than_5 = 0
# mult_of_num_more_than_7 = 1
# count_0_or_5 = 0
# while n > 0:
#     last_digit = n % 10
#     if last_digit == 3:
#         count_of_3 += 1
#     if last_digit == my_last_digit:
#         count_of_last_digit += 1
#     if last_digit % 2 == 0:
#         even += 1
#     if last_digit > 5:
#         sum_of_num_more_than_5 += last_digit
#     if last_digit > 7:
#         mult_of_num_more_than_7 *= last_digit
#     if last_digit == 0 or last_digit == 5:
#         count_0_or_5 += 1
#     n //= 10
# print(count_of_3)
# print(count_of_last_digit)
# print(even)
# print(sum_of_num_more_than_5)
# print(mult_of_num_more_than_7)
# print(count_0_or_5)

n = 33
for a in range(1, n):
    for b in range(a, n):
        e = a ** 3 + b ** 3
        for c in range(2, n):
            for d in range(c, n):
                if e == c ** 3 + d ** 3:
                    if a != b and a != c and b != c and b != d:
                        print(a, b, c, d, e)

