from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))[1:]
person = [0] * (n + 1)
party = [list(map(int, input().split()))[1:] for _ in range(m)]
# print(arr)
for a in arr: person[a] = 1
arr = deque(arr)
while arr:
    x = arr.popleft()
    cnt = []
    for i in range(len(party)):
        if x in party[i]:
            for r in party[i]:
                if person[r] == 0:
                    arr.append(r)
                    person[r] = 1
            cnt.append(i)
    cnt.sort(reverse=True)
    for y in cnt:
        del party[y]
print(len(party))
