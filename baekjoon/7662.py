import sys, heapq

T = int(input())

for _ in range(T):
    length = 0
    minHeap, maxHeap = [], []
    visited = [False] * 1_000_001
    
    K = int(input())
    for key in range(K):
        command, num = sys.stdin.readline().split()
        
        if command == 'I':
            heapq.heappush(minHeap, (int(num), key))
            heapq.heappush(maxHeap, ((-1) * int(num), key))
            visited[key] = True
            length += 1
        else:
            if length == 0:
                continue
            if num == '-1':
                delNode = heapq.heappop(minHeap)
                while not visited[delNode[1]]:
                    delNode = heapq.heappop(minHeap)
                visited[delNode[1]] = False
                length -= 1
            else:
                delNode = heapq.heappop(maxHeap)
                while not visited[delNode[1]]:
                    delNode = heapq.heappop(maxHeap)
                visited[delNode[1]] = False
                length -= 1

    while minHeap and not visited[minHeap[0][1]]:
        heapq.heappop(minHeap)
    while maxHeap and not visited[maxHeap[0][1]]:
        heapq.heappop(maxHeap)

    if minHeap and maxHeap:
        print(maxHeap[0][0] * -1, minHeap[0][0])
    else:
        print('EMPTY')