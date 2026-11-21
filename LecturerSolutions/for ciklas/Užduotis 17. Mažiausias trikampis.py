import math
import sys

sys.stdin = open("U1.txt", "r")
sys.stdout = open("U1rez.txt", "w")

n = int(input())
min_area = None

for i in range(n):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    a = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    b = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
    c = math.sqrt((x1 - x3)**2 + (y1 - y3)**2)
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))

    if s == 0:
        continue

    if min_area is None or s < min_area:
        min_area = s

if min_area is not None:
    print(f"{min_area:.2f}")
else:
    print("No")