from itertools import combinations

n = int(input())
graph = [list(map(int, input().split())) for __ in range(n)]

answer = int(1e9)

for start in combinations(range(1, n+1), n//2):
    link = [x for x in range(1, n+1) if x not in start]

    total1 = 0
    for i, x in enumerate(start):
        for j, y in enumerate(start):
            if i < j:
                total1 += graph[x-1][y-1] + graph[y-1][x-1]

    total2 = 0
    for i, x in enumerate(link):
        for j, y in enumerate(link):
            if i < j:
                total2 += graph[x-1][y-1] + graph[y-1][x-1]

    answer = min(answer, abs(total1-total2))

print(answer)