a1, a2, b1, b2 = int(input()), int(input()), int(input()), int(input())
if abs(b1 - a1) < 3 and abs(b2 - a2) < 3 and abs(b1 - a1) + abs(b2 - a2) == 3:
    print("YES")
else:
    print("NO")
