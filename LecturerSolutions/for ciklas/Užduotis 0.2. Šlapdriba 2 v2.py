import sys

sys.stdin = open("U1.txt", "r")
sys.stdout = open("U1rez.txt", "w")

n = int(input())
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i, '*0')
    else:
        print(i, '**')