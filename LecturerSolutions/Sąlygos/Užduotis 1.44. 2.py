s0, v1, v2, t = map(int, input().split())

s1 = v1 * t
s2 = v2 * t
s = s0 + s1 - s2

# 260 km. Niekada nepavys
# 50 km. Pavys
# 0 km. Pasivijo
# 10 km. Aplenke

if s >= s0:
    print(s, "km. Niekada nepavys")
elif s == 0:
    print(s, "km. Pasivijo")
elif s0 > s > 0:
    print(s, "km. Pavys")
else:
    print(-s, "km. Aplenke")