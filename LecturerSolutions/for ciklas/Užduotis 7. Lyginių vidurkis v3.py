import sys

sys.stdin = open("U1.txt", "r")
sys.stdout = open("U1rez.txt", "w")

n = int(input())
c = 0
s = 0
for i in range(2, n + 1, 2):
    c += 1
    s += i

if c > 0:
    print(s // c)
else:
    print("NO")