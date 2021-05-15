from collections import deque

N, K = map(int, input().split())
visited = [0] * 100_001

queue = deque([(N, 0)])
visited[N] = 1

while queue:
    if queue[0][0] == K:
        break
    node, cnt = queue.popleft()
    
    v1, v2, v3 = node - 1, node + 1, node * 2
    if v1 >= 0 and not visited[v1]:
        queue.append((v1, cnt + 1))
        visited[v1] = 1
    if v2 <= 100_000 and not visited[v2]:
        queue.append((v2, cnt + 1))
        visited[v2] = 1
    if v3 <= 100_000 and not visited[v3]:
        queue.append((v3, cnt + 1))
        visited[v3] = 1

print(queue[0][1])