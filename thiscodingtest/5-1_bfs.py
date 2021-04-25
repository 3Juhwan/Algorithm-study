from collections import deque 

N, M = map(int, input().split())
input_data = []
for _ in range(N):
    input_data.append(list(map(int, input())))
    
result = 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def bfs(data, start):
    queue = deque([start])
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            # Good
            if nx <= -1 or nx >= N or ny <= -1 or ny >= M:
                continue
            if input_data[nx][ny] == 0:
                input_data[nx][ny] = 1
                queue.append((nx, ny))
            
            # Not Good
            """
            if nx >= 0 and nx < N and ny >= 0 and ny < M:
                if input_data[nx][ny] == 0:
                    queue.append((nx, ny))
                    input_data[nx][ny] = 1
            """
            
for i in range(N):
    for j in range(M):
        if input_data[i][j] == 0:
            locat = (i, j)
            bfs(input_data, locat)
            result += 1
            
print(result)