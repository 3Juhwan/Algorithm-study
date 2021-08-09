import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


t = int(input())
for __ in range(t):
    n, d, c = map(int, input().split())
    
    graph = [[] for __ in range(n + 1)]
    distance = [INF] * (n + 1)
    
    for __ in range(d):
        a, b, time = map(int, input().split())
        graph[b].append((a, time))
    
    dijkstra(c)
    
    distance = [x for x in distance if x != INF]
    
    print(len(distance), max(distance))