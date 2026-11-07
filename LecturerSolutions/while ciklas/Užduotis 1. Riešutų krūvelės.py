k1 = int(input())
n = 0

while k1 > 0:
    if k1 % 2 != 0:
        k1 -= 1
    else:
        k1 //= 2
    n += 1

print(n)