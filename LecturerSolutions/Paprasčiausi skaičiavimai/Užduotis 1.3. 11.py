s0, v1, v2, t = map(float, input().split())
s = abs(s0 - (v1 + v2) * t)
print(f"{s:g} km")