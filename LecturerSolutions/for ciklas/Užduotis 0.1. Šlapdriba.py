import sys

sys.stdin = open("U1.txt", "r")
sys.stdout = open("U1rez.txt", "w")

n = int(input())
for i in range(n):
    if i % 2 == 0:
        print('*0')
    else:
        print('**')