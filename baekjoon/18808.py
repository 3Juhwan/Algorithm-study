import sys
input = sys.stdin.readline

# turn sticker 90
def rotate_90(sticker):
    x, y = len(sticker), len(sticker[0])
    new_sticker = [[sticker[-j + x - 1][i] for j in range(x)] for i in range(y)]
    return new_sticker


def canStick(sticker, now):
    x, y = len(sticker), len(sticker[0])
    for i in range(x):
        for j in range(y):
            if sticker[i][j]:
                if graph[now[0]+i][now[1]+j]:
                    return False
    return True

def stick(sticker, now):
    x, y = len(sticker), len(sticker[0])
    for i in range(x):
        for j in range(y):
            if sticker[i][j]:
                graph[now[0]+i][now[1]+j] = sticker[i][j]

def run(sticker):
    x, y = len(sticker), len(sticker[0])
    for i in range(n - x + 1):
        for j in range(m - y + 1):
            if canStick(sticker, (i, j)):
                stick(sticker, (i, j))
                return True
    return False
    

# input
n, m, k = map(int, input().split())
stickers = []
for __ in range(k):
    x, __ = map(int, input().split())
    stickers.append([list(map(int, input().split())) for __ in range(x)])

# notebook
graph = [[0] * m for __ in range(n)]

for i in range(k):
    sticker = stickers[i]
    for __ in range(4):
        if run(sticker):
            break
        sticker = rotate_90(sticker)

print(len([x for row in graph for x in row if x]))