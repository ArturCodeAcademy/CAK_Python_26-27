n = int(input())
i = 1
while i * i <= n:
    j = i
    while i * i + j * j <= n:
        if i * i + j * j == n:
            print(f"TAIP")
            exit()
        j += 1
    i += 1

print(f"NE")