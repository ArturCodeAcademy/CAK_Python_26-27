for i in range(1, 11):
    for j in range(1, 11):
        r = i * j
        if r < 10:
            print(f"   {r}", end="")
        elif r < 100:
            print(f"  {r}", end="")
        else:
            print(f" {r}", end="")
    print()