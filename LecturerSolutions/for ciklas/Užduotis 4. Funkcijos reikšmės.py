import sys

sys.stdin = open("U1.txt", "r")
sys.stdout = open("U1rez.txt", "w")

a, b, c = map(int, input().split())
for x in range(-3, 4):
    y = x ** 2 * a + x * b + c
    print(f"Kai x={x}, tai y={y}")