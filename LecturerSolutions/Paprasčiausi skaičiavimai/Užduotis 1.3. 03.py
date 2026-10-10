s = int(input())

m = s // 60 % 60
h = s // 60 // 60
# print(h, "val.", m, "min.")
print(f"{h} val. {m} min.")