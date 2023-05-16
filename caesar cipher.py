# Целые числа (тип int);
# Модульная арифметика;
# Переменные;
# Ввод / вывод данных (функции input() и print());
# Условный оператор (if/elif/else);
# Цикл for/while;
# Строковые методы.

# str1 = "Блажен, кто верует, тепло ему на свете!"
str1 = "To be, or not to be, that is the question!"
str2 = ""
n = 17
for i in str1:
    if i not in " ,!":
        str2 += chr(((ord(i) + n) % 26))
        # elif ord(i) <= 90:
        #     str2 += chr(65 + n - 90 + ord(i))
        # elif ord(i) <= 122 - n:
        #     str2 += chr(ord(i) + n)
        # elif ord(i) <= 122:
        #     str2 += chr(97 + n - 122 + ord(i))
        # elif ord(i) <= 1071 - n:
        #     str2 += chr(ord(i) + n)
        # elif ord(i) <= 1071:
        #     str2 += chr(1040 + n - 1071 + ord(i))
        # elif ord(i) <= 1103 - n:
        #     str2 += chr(ord(i) + n)
        # else:
        #     str2 += chr(1072 + n - 1103 + ord(i))
    else:
        str2 += i
print(ord("А"), ord("Я"))
print(ord("а"), ord("я"))
print(ord("A"), ord("Z"))
print(ord("a"), ord("z"))
print(str2)
