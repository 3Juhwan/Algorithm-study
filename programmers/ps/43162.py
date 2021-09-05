def dfs(computers, visited, x):
    for i in range(len(computers)):
        if not visited[i] and computers[x][i]:
            visited[i] = 1
            dfs(computers, visited, i)

def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        for j in range(i, n):
            if not visited[i] and computers[i][j]:
                visited[i] = 1
                dfs(computers, visited, j)
                answer += 1
    return answer