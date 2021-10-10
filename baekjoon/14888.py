from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
p, mi, mu, d = map(int, input().split())

max_num, min_num = -int(1e9), int(1e9)


q = deque([(1, numbers[0], p, mi, mu, d)])
while q:
    idx, total, p, mi, mu, d = q.popleft()
    if idx == n:
        max_num = max(max_num, total)
        min_num = min(min_num, total)
        continue
    if p:
        q.append((idx+1, total+numbers[idx], p-1, mi, mu, d))
    if mi:
        q.append((idx+1, total-numbers[idx], p, mi-1, mu, d))
    if mu:
        q.append((idx+1, total*numbers[idx], p, mi, mu-1, d))
    if d:
        tmp = -(abs(total)//abs(numbers[idx])) if total*numbers[idx] < 0 else abs(total)//abs(numbers[idx])
        q.append((idx+1, tmp, p, mi, mu, d-1))

print(max_num)
print(min_num)