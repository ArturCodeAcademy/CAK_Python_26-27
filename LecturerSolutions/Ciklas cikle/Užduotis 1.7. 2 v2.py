n = int(input())
result = "NE"
i = 1
while i * i <= n and result == "NE":
    j = i
    while i * i + j * j <= n:
        if i * i + j * j == n:
            result = "TAIP"
            break
        j += 1
    i += 1

print(f"{result}")