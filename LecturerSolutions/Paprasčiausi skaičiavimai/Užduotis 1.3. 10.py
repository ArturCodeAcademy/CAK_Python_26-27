kg, price = map(float, input().split())
kg_price = price / kg
_100_g_price = kg_price / 10
lt = int(_100_g_price)
ct = int((_100_g_price - lt) * 100)
print(f"{lt} Lt {ct} ct")