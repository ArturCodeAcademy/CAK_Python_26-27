import math

r1, r2 = map(float, input().split())
s = (r1 ** 2 - r2 ** 2) * math.pi
print(f"{s:.0f} kv. mm")