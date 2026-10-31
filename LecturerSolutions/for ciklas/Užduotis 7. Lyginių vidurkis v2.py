import sys

sys.stdin = open("U1.txt", "r")
sys.stdout = open("U1rez.txt", "w")

n = int(input())
if n == 1:
    print("NO")
else:
    print((n - n % 2) // 2 + 1)