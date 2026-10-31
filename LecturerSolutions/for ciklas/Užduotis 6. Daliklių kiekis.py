import sys

sys.stdin = open("U1.txt", "r")
sys.stdout = open("U1rez.txt", "w")

n = int(input())
d = 1
for i in range(1, n // 2 + 1):
    if n % i == 0:
        d += 1
print(d)