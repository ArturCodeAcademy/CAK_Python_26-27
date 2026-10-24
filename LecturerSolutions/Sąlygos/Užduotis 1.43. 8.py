a1, b1, a2, b2, a3, b3 = map(int, input().split())

s1 = a1 * b1 / 2
s2 = a2 * b2 / 2
s3 = a3 * b3 / 2

if s1 == s2 or s1 == s3 or s2 == s3:
    print("Taip")
else:
    print("Ne")