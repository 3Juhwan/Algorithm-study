N = int(input())
arr = [0]
for _ in range(N):
    arr.append(int(input()))

arr.sort()

result = 0
for i in range(1, N + 1):
    result += abs(i - arr[i])

print(result)