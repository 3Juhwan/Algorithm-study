import sys
input = sys.stdin.readline

def isValidRoad(N, L, road):
    bump = -1
    for i in range(1, N):
        diff = road[i] - road[i - 1]
        if diff == 0:
            continue
        elif diff == -1:
            for j in range(i, i + L):
                if j >= N or not road[i - 1] - road[j] == 1:
                    return False
            bump = i + L - 1
        elif diff == 1:
            for j in range(i - 1, i - L - 1, -1):
                if j < 0 or j <= bump or not road[i] - road[j] == 1:
                    return False
            bump = i - 1
        else:
            return False
    return True

def rotate_a_matrix_by_90_degree(a):
    row_length = len(a)
    column_length = len(a[0])

    res = [[0] * row_length for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            res[c][row_length - 1 - r] = a[r][c]

    return res

# Run
N, L = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip().split())))

result = 0
for i in range(N):
    if isValidRoad(N, L, graph[i]):
        result += 1

# 벡터 회전 구현
graph = rotate_a_matrix_by_90_degree(graph)

for i in range(N):
    if isValidRoad(N, L, graph[i]):
        result += 1

print(result)