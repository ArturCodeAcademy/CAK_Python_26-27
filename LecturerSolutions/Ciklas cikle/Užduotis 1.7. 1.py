n = int(input())
a = n // 3
b = 0

while True:
    # print(f"Alisa - {a} ({a * 3})")
    b = 0
    # print(f"\tBazilijus - {b} ({5 * b}) -> {3 * a - 5 * b}")
    while 3 * a - 5 * b > n:
        b += 1
        # print(f"\tBazilijus - {b} ({5 * b}) -> {3 * a - 5 * b}")

    if 3 * a - 5 * b == n:
        print(f"Alisa - {a}, Bazilijus - {b}")
        break

    a += 1
