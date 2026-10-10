p = int(input())

d = p // 15
b = (p % 15) // 3
p %= 3

print(f"{d} D, {b} B, {p} P")