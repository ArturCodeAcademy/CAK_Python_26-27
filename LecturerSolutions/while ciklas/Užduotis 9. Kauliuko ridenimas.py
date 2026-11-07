t = int(input())
f1 = 0
f2 = 0

while f1 < t and f2 < t:
    r1, r2 = map(int, input().split())
    f1 += r1
    f2 += r2

if f1 >= t and f2 >= t:
    print("Zaidimas baigesi lygiosiomis")
elif f1 >= t:
    print("Zaidima laimi 1 draugas")
else:
    print("Zaidima laimi 2 draugas")