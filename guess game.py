import random

print("Играем в числовую угадайку")


def is_valid(n):
    return n.isdigit() and 0 < int(n) < max_n


while True:
    max_n = int(input("Введите максимальное число, до которого я загадаю _"))
    number = random.randint(1, max_n)
    count = 0
    while number:
        print("Введите число от 1 до", max_n)
        num = input()
        count += 1
        if is_valid(num):
            num = int(num)
            if num < number:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            elif num > number:
                print('Ваше число больше загаданного, попробуйте еще разок')
            else:
                print('Вы угадали, поздравляем!')
                print("Число попыток ", count)
                print('Спасибо, что играли в числовую угадайку!')
                print()
                break
        else:
            print(f"А может быть все-таки введем целое число от 1 до ", max_n, "?")

    answer = input("Хотите продолжить? 0 - нет, 1 - да ")
    if int(answer) == 0:
        break
