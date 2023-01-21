str_1 = 'бзлмтфхш'
str_2 = 'юы'
str_3 = 'бзжлмтфцш'
for i in str_1:
    for j in str_2:
        for k in str_3:
            print('е' + i + 'р' + j + k, end=' ')
            if k == 'т':
                print()
print()
str_1 = 'бзлмтфцш'
str_2 = 'юэы'
for i in str_1:
    for j in str_2:
        print(i + j + 'рхе', end=' ')


