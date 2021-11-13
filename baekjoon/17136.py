import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for __ in range(10)]
paper = [0]*6
visited = [[[0]*55555 for __ in range(10)] for __ in range(10)]


def getNext(board, x, y):
    while x < 10 and y < 10:
        if board[x][y]:
            return (x, y)
        x, y = (x, y+1) if y+1 < 10 else (x+1, 0)
    return (x, y)


def isCover(board, size, x, y):
    if x+size > 10 or y+size > 10:
        return 0
    for i in range(size):
        for j in range(size):
            if not board[x+i][y+j]:
                return 0
    for i in range(size):
        for j in range(size):
            board[x+i][y+j] = 0
    return 1


def answer(board, x, y):
    global result
    if x > 9 or y > 9:
        result = min(result, sum(paper))
        return

    if sum(paper) >= result:
        return

    if board[x][y]:
        for i in range(1, 6):
            if paper[i] == 5:
                continue
            if isCover(board, i, x, y):
                paper[i] += 1
                nx, ny = getNext(board, x, y)
                tmp = int(''.join([str(q) for q in paper]))
                if not visited[x][y][tmp]:
                    visited[x][y][tmp] = 1
                    answer(board, nx, ny)
                for q in range(i):
                    for w in range(i):
                        board[x+q][y+w] = 1
                paper[i] -= 1
    else:
        nx, ny = getNext(board, x, y)
        answer(board, nx, ny)
    return


result = 101
answer(board, 0, 0)
print(result if result != 101 else -1)