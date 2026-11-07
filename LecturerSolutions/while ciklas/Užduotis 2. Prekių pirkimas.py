p, k, s = map(int, input().split())
n = 0

while s >= p:
    s -= p
    p += k
    n += 1

print("Pirkejo nupirktu prekiu kiekis:", n)