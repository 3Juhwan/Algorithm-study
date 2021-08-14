import sys
input = sys.stdin.readline

def getMinNumToRecolor(x, y):
    global result
    cnt1, cnt2 = 0, 0
    
    for i in range(x, x + 8):
        for j in range(y, y + 8):
            if (i + j) % 2:
                if graph[i][j] == 'W':
                    cnt1 += 1
                else:
                    cnt2 += 1
            else:
                if graph[i][j] == 'B':
                    cnt1 += 1
                else:
                    cnt2 += 1
    
    result = min(result, cnt1, cnt2)

n, m = map(int, input().split())
graph = [list(input().rstrip()) for __ in range(n)]
result = 64

for i in range(len(graph) - 7):
    for j in range(len(graph[0]) - 7):
        getMinNumToRecolor(i, j)

print(result)