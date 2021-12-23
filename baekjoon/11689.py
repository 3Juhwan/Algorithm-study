from math import sqrt
n = int(input())
a = []
c, r = n, n
for i in range(2, int(sqrt(n))+1):
    if c % i == 0:
        while c % i == 0:
            c //= i
        r = r * (i-1) // i
if c > 1:
    r = r * (c-1) // c
print(r)