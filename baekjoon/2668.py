import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + [int(input()) for __ in range(n)]


def dfs(x):
    if t_visited[arr[x]]:
        return []

    t_visited[arr[x]] = 1
    return [arr[x]] + dfs(arr[x])


visited = [0] * (n+1)
answer = []
for i in range(1, n+1):
    t_visited = visited[:]
    tmp = dfs(i)
    if not t_visited[i]:
        continue
    for x in tmp:
        visited[x] = 1
    answer += tmp

print(len(answer))
for x in sorted(answer):
    print(x)