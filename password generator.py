import random


def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += random.choice(chars)
    print(password)


count_of_passwords = int(input("Сколько паролей тебе нужно? "))
need_dig = int(input("Включать ли цифры? 1 -да, 0 - нет "))
need_upper = int(input("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? 1 -да, 0 - нет "))
need_lower = int(input("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? 1 -да, 0 - нет "))
need_symbols = int(input("Включать ли символы !#$%*+-=?@^_ 1 -да, 0 - нет "))
exclude_characters = int(input("Исключать ли неоднозначные символы il1Lo0O ? 1 -да, 0 - нет "))

digits = "0123456789"
lower_letters = "abcdefghijklmnopqrstuvwxyz"
upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%*+-=?@^_"

my_chars = digits * need_dig + lower_letters * need_lower + upper_letters * need_upper + punctuation * need_symbols

if exclude_characters:
    for i in 'il1Lo0O':
        my_chars = my_chars.replace(i, '')

my_length = int(input('Какая длина пароля, символов? '))

for i in range(count_of_passwords):
    generate_password(my_length, my_chars)
