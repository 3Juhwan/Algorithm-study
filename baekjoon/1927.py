import sys, heapq

heap = []

N = int(input())

for _ in range(N):
    x = int(sys.stdin.readline())

    if x > 0:
        heapq.heappush(heap, x)
    else:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
