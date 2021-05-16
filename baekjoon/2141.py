import sys
input = sys.stdin.readline

N = int(input())
arr, total = [], 0
for __ in range(N):
    X, A = map(int, input().split())
    total += A
    arr.append((X, A))
    
arr.sort(key=lambda x: x[0])

if total % 2 == 1:
    total += 1

t = 0    
for i in arr:
    t += i[1]
    if t >= total // 2:
        print(i[0])
        break
