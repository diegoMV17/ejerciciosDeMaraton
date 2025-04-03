import math

Y, W = map(int, input().split())
best = max(Y, W)
casos_favorables = 6 - best + 1
gcd = math.gcd(casos_favorables, 6)
print(f"{casos_favorables // gcd}/{6 // gcd}")
