import sys
input = sys.stdin.readline

n, b = map(int, input().split())
matrix = [list(map(lambda x: int(x)%1000, input().split())) for __ in range(n)]


def product(m1, m2):
    result = [[0] * n for __ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += m1[i][k] * m2[k][j]

    for i in range(n):
        for j in range(n):
            result[i][j] %= 1000
    return result


def answer(matrix, n):
    if n == 1:
        return matrix

    result = answer(matrix, n//2)
    if n%2 == 0:
        return product(result, result)
    else:
        return product(product(result, result), matrix)


result = answer(matrix, b)
for x in result: print(*x)