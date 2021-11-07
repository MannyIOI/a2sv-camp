a, b, c, d = [int(i) for i in input().split()]
num = a * d
den = (b * c) + (d * a) - (a * c)
print(num / den)