import sys

sys.stdin = open("U1.txt", "r")
sys.stdout = open("U1rez.txt", "w")

a, b = map(int, input().split())
for i in range(a, b + 1):
    print(i ** 2)