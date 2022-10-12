#  Сортируем три стоки по длине
lst = sorted([len(input()), len(input()), len(input())])
print(lst[0])
print(lst[2])

# проверим, можно ли из длин строк составить арифметическую прогресию
print("YES" if lst[2] - lst[1] == lst[1] - lst[0] else "NO")

n = input()
print("YES" if "суббота" in n or "воскресенье" in n else "NO")
