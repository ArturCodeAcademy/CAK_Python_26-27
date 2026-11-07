p, k, s = map(int, input().split())
n = 0

while s >= p + k * n:
    s -= p + k * n
    n += 1

print("Pirkejo nupirktu prekiu kiekis:", n)