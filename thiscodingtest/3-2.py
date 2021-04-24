N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
digit = data[-1] * K + data[-2]

d_num = M // (K + 1)
M %= (K + 1)
result = digit * d_num + M * data[-1]

print(result)