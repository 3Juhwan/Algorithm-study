import sys
input = sys.stdin.readline

n = int(input())
papers = [list(map(int, input().split())) for __ in range(n)]

answer = [0]*2


def cntPapers(x, y, n):
    if isSame(x, y, n):
        return 0
    else:
        for i in range(2):
            for j in range(2):
                cntPapers(x+n//2*i, y+n//2*j, n//2)


def isSame(x, y, n):
    blue, white = [0]*2
    for i in range(x, x+n):
        for j in range(y, y+n):
            if papers[i][j] == 0:
                white += 1
            else:
                blue += 1
            if blue and white:
                return False

    if white: answer[0] += 1
    else: answer[1] += 1
    return True


cntPapers(0, 0, n)
for x in answer: print(x)