from copy import deepcopy
import sys
input = sys.stdin.readline

n, q = map(int, input().split())
arr = [list(map(int, input().split())) for __ in range(n)]
logs = deepcopy(arr)
logs.sort()

move = [logs[0][:2]]
# sweeping
for i in range(1, n):
    now = move[-1][1]
    next = logs[i][0]
    if now >= next:
        s, e = move.pop()
        e = e if e >= logs[i][1] else logs[i][1]
        move.append([s, e])   # move[i]이 앞에보다 당연히 크다
    else:
        move.append(logs[i][:2])

# run
for __ in range(q):
    a, b = map(int, input().split())
    tmp = sorted([arr[a-1], arr[b-1]])
    s, e = tmp[0][0], tmp[1][1]

    flag = 0
    for x, y in move:
        if x <= s and e <= y:
            flag = 1
            break

	print(flag)