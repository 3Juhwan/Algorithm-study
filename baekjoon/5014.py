from collections import deque
import sys
input = sys.stdin.readline

def bfs(S):
    visited = [0] * (F + 1)
    q = deque([(0, S)])

    while q:
        cnt, now = q.popleft()
        if now == G:
            return cnt

        floors = [now + U, now - D]
        for i in floors:
            if 0 < i <= F and not visited[i]:
                visited[i] = 1
                q.append((cnt + 1, i))

    return -1


F, S, G, U, D = map(int, input().split())
answer = bfs(S)
print(answer if not answer == -1 else "use the stairs")