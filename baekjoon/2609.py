n, m = map(int, input().split())
if n > m:
    n, m = m, n

for i in range(1, n):
    if n % i == 0 and m % i == 0:
        mid = i

print(mid)
print(int(n*m/mid))
