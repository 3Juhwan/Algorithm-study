n, m = map(int, input().split())
num = list(i - n * m for i in map(int, input().split()))
for i in num:
    print(i, end=' ')
