from copy import deepcopy
from collections import deque
import sys
input = sys.stdin.readline

def getMaxNum(graph):
    return max([x for row in graph for x in row])

def up(board):
    graph = [[0] * n for _ in range(n)]
    for i in range(n):
        # 행에 있는 모든 수 추출
        row = [board[x][i] for x in range(n) if board[x][i]]
        
        # 행을 차례로 더하기
        rrow = []
        s, e = 0, 1
        while e < len(row):
            if row[s] == row[e]:
                rrow.append(row[s] * 2)
                s, e = e + 1, e + 2
            else:
                rrow.append(row[s])
                s, e = e, e + 1
        if s < len(row):    # 이부분 주의
            rrow.append(row[s])
        
        for x in range(len(rrow)):
            graph[x][i] = rrow[x]
    
    return graph

def down(board):
    graph = [[0] * n for _ in range(n)]
    for i in range(n):
        # 행에 있는 모든 수 추출
        row = [board[x][i] for x in range(n) if board[x][i]]
        row.reverse()
        
        # 행을 차례로 더하기
        rrow = []
        s, e = 0, 1
        while e < len(row):
            if row[s] == row[e]:
                rrow.append(row[s] * 2)
                s, e = e + 1, e + 2
            else:
                rrow.append(row[s])
                s, e = e, e + 1
        if s < len(row):    # 이부분 주의
            rrow.append(row[s])
        
        for x in range(len(rrow)):
            graph[n - x - 1][i] = rrow[x]
    
    return graph

def left(board):
    graph = [[0] * n for _ in range(n)]
    for i in range(n):
        # 행에 있는 모든 수 추출
        row = [board[i][x] for x in range(n) if board[i][x]]
        
        # 행을 차례로 더하기
        rrow = []
        s, e = 0, 1
        while e < len(row):
            if row[s] == row[e]:
                rrow.append(row[s] * 2)
                s, e = e + 1, e + 2
            else:
                rrow.append(row[s])
                s, e = e, e + 1
        if s < len(row):    # 이부분 주의
            rrow.append(row[s])
        
        for x in range(len(rrow)):
            graph[i][x] = rrow[x]
    
    return graph

def right(board):
    graph = [[0] * n for _ in range(n)]
    for i in range(n):
        # 행에 있는 모든 수 추출
        row = [board[i][x] for x in range(n) if board[i][x]]
        row.reverse()
        
        # 행을 차례로 더하기
        rrow = []
        s, e = 0, 1
        while e < len(row):
            if row[s] == row[e]:
                rrow.append(row[s] * 2)
                s, e = e + 1, e + 2
            else:
                rrow.append(row[s])
                s, e = e, e + 1
        if s < len(row):    # 이부분 주의
            rrow.append(row[s])
        
        for x in range(len(rrow)):
            graph[i][n - x - 1] = rrow[x]
    
    return graph

def bfs(graph):
    result = 0
    q = deque([(graph, 0)])
    
    while q:
        now, cnt = q.popleft()
        result = max(result, getMaxNum(now))
        if cnt == 5:
            continue
            
        q.append((up(now), cnt + 1))
        q.append((down(now), cnt + 1))
        q.append((left(now), cnt + 1))
        q.append((right(now), cnt + 1))
        
    return result

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

print(bfs(graph))
