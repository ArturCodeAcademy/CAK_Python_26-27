import sys

sys.stdin = open("U1.txt", "r")
sys.stdout = open("U1rez.txt", "w")

n = int(input())
if n == 1:
    print("NO")
else:
    c = 0
    s = 0
    for i in range(2, n + 1):
        if i % 2 == 0:
            c += 1
            s += i

    print(s // c)