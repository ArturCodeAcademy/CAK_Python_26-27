import sys

sys.stdin = open("U1.txt", "r")
sys.stdout = open("U1rez.txt", "w")

n = int(input())
print(",".join(map(str, list(range(1, n + 1, 2)) + list(range(2, n + 1, 2)))))