N, M = map(int, input().split())
cntNum = 0

tile = []
for i in range(N):
    tile.append(list(input()))

for i in range(N):
    j = 0
    while j < M:
        if tile[i][j] == '-':
            while j < M - 1 and tile[i][j+1] == '-':
                j += 1
            cntNum += 1
        j += 1

for i in range(M):
    j = 0
    while j < N:
        if tile[j][i] == '|':
            while j < N - 1 and tile[j+1][i] == '|':
                j += 1
            cntNum += 1
        j += 1

print(cntNum)
