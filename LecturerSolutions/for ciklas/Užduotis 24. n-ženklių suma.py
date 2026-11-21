import sys

sys.stdin = open("U1.txt", "r")
sys.stdout = open("U1rez.txt", "w")

n = int(input())

if n < 4:
    s = 0
    for i in range(10 ** (n - 1), 10 ** n):
        s += i
    print(s)
else:
    print(494, end="")
    for i in range(n - 3):
        print(9, end="")
    print(55, end="")
    for i in range(n - 2):
        print(0, end="")