m, n = map(int, input().split())

packed = n // m
unpacked = n % m

print("Pilnu dezuciu skaicius:", packed)
print("Nesupakuotu puodeliu skaicius:", unpacked)
