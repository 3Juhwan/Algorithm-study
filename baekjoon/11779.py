import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    route[start].append(start)
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                route[i[0]] = route[now][:] + [i[0]]

# INPUT
n = int(input())
m = int(input())
graph = [[] for __ in range(n + 1)]
for __ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
start, end = map(int, input().split())

distance = [INF] * (n + 1)
route = [[] for __ in range(n + 1)]

dijkstra(start)

print(distance[end])
print(len(route[end]))
print(*route[end])