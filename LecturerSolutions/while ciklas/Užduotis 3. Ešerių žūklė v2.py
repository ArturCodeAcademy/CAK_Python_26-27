m = -1
total = 0
count = 0
while m != 0:
    m = int(input())
    total += m
    if m > 100:
        count += 1

print("Zuvu mase:", total)
print("Rimtu zuvu kiekis:", count)