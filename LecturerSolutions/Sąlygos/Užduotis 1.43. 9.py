s1, v1, s2, v2 = map(int,input().split())

if s1 / v1 > s2 / v2:
    print("Pirmoji didesne")
elif s1 / v1 == s2 / v2:
    print("Trupmenos lygios")
else:
    print("Antroji didesne")