import math
A, B = map(int, input().split())
B //= A
y = 1
for x in range(1, B + 1):
    if B % x == 0 and math.gcd(x, B // x) == 1:
        if y * x >= B:
            break
        y = x
print(A * y, A * (B // y))