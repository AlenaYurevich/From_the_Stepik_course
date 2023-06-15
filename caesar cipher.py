# Целые числа (тип int);
# Модульная арифметика;
# Переменные;
# Ввод / вывод данных (функции input() и print());
# Условный оператор (if/elif/else);
# Цикл for/while;
# Строковые методы.


def caesar_code(text1, step, encrypted_text=''):
    a = 'abcdefghijklmnopqrstuvwxyz'
    for i in text1:
        if i.lower() in a:
            encrypted_text += a[a.find(i.lower()) - 26 + step]
        else:
            encrypted_text += i
    return encrypted_text.capitalize()


text1 = 'To be, or not to be, that is the question!'
step = 17

print(caesar_code(text1, step))


def caesar_code_rus(text2, step, encrypted_text=''):
    a = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    for i in text2:
        if i.lower() in a:
            encrypted_text += a[a.find(i.lower()) - step]  # обратный сдвиг
        else:
            encrypted_text += i
    return encrypted_text.capitalize()


text2 = 'Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг.'
step = 7

print(caesar_code_rus(text2, step))


def caesar_code(text, step, encrypted_text=''):
    for i in text:
        if i.isalpha():
            if (ord(i.lower()) - ord('z') + step) > 0:
                encrypted_text += chr(ord(i.lower()) - (26 - step))
            else:
                encrypted_text += chr(ord(i.lower()) + step)
        else:
            encrypted_text += i
    return encrypted_text.capitalize()


text = 'Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.'
step = 25
print(caesar_code(text, step))


def caesar_code(text2, step, encrypted_text=''):
    a = 'abcdefghijklmnopqrstuvwxyz'
    for i in text2:
        if i.lower() in a:
            encrypted_text += a[a.find(i.lower()) - step]  # обратный сдвиг
        else:
            encrypted_text += i
    return encrypted_text.capitalize()


# text2 = 'Hawnj pk swhg xabkna ukq nqj.'
# step = 1
# for i in range(1, 26):
#     print(step)
#     print(caesar_code(text2, step))
#     step += 1


# На вход программе подается строка текста на английском языке, в которой нужно зашифровать все слова. Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова). Строчные буквы при этом остаются строчными, а прописные – прописными. Гарантируется, что между различными словами присутствует один пробел.
def caesar_code_3(text, encrypted_text=''):
    a = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    words = text.split(" ")
    for word in words:
        step = len([1 for i in word if i.isalpha()])
        for i in word:
            if i == i.lower():
                if i.lower() in a:
                    encrypted_text += a[a.find(i.lower()) - 26 + step]  # сдвиг вправо
                else:
                    encrypted_text += i
            else:
                encrypted_text += a[a.find(i.lower()) - 26 + step].upper()  # сдвиг вправо
        encrypted_text += ' '
    res += encrypted_text
    print(res)


text = 'Day, mice. "Year" is a mistake!'
caesar_code_3(text)
