from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

target = ''.join([''.join(input().split()) for __ in range(3)])
target = target.replace('0', '9')

visited = {123456789: 0}


def getNexts(num):
    s = str(num)
    arr = [list(s[i*3:i*3+3]) for i in range(3)]
    x, y = 0, 0
    for i in range(3):
        for j in range(3):
            if arr[i][j] == '9':
                x, y = i, j
                break

    result = []
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < 3 and 0 <= ny < 3:
            stmp = list(s[:])
            stmp[x*3+y], stmp[nx*3+ny] = stmp[nx*3+ny], stmp[x*3+y]
            qwe = int(''.join(stmp))
            if qwe not in visited:
                result.append(qwe)

    return result


def answer(t):
    q = deque([123456789])
    while q:
        x = q.popleft()
        if x == t:
            return visited[x]

        nexts = getNexts(x)

        for next in nexts:
            if next not in visited:
                visited[next] = visited[x] + 1
                q.append(next)
    return -1


print(answer(int(target)))