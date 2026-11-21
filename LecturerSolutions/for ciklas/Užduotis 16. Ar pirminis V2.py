import sys

sys.stdin = open("U1.txt", "r")
sys.stdout = open("U1rez.txt", "w")

n = int(input())

if n <= 1:
    print("NE")
else:
    found = False
    for i in range(2, n):
        if n % i == 0:
            print("NE")
            found = True
            break
    if not found:
        print("TAIP")
