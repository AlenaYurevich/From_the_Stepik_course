a1, a2, b1, b2 = int(input()), int(input()), int(input()), int(input())
if abs(b1 - a1) == abs(b2 - a2) or a1 == b1 or a2 == b2:
    print("YES")
else:
    print("NO")
