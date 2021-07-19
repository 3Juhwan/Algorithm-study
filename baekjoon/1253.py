n = int(input())
arr = list(map(int, input().split()))

hash = {}

for i in range(n - 1):
    for j in range(i + 1, n):
        num = arr[i] + arr[j]
        if num in hash:
            hash[num].append((i, j))
        else: 
            hash[num] = [(i, j)]
cnt = 0
for i in range(n):
    if arr[i] in hash:
        for a in hash[arr[i]]:
            if i not in a:
                cnt += 1
                break
        
print(cnt)