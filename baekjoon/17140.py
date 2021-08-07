import sys
input = sys.stdin.readline

def rotate_a_matrix_by_90_degree(a):
    row_length = len(a)
    column_length = len(a[0])

    res = [[0] * row_length for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            res[c][r] = a[r][c]

    return res

def get_new_sorted_array(array):
    sorted_dict = {}
    
    # 딕셔너리에 전부 넣기
    for x in array:
        if not x:
            continue
        if x in sorted_dict:
            sorted_dict[x] += 1
        else:
            sorted_dict[x] = 1
    
    sorted_list = sorted(list(sorted_dict.items()), key=lambda x: (x[1], x[0]), reverse=True)
    
    result = []
    
    # 길이가 100 넘어가면 100까지만 주기
    while sorted_list and len(result) < 100:
        x, y = sorted_list.pop()
        result.append(x)
        result.append(y)
    
    return result

r, c, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(3)]

time = -1
# 100초가 지나면 종료
for i in range(100):
    flag = 0
    row_len, column_len = len(graph), len(graph[0])
    
    # 정답 확인
    if row_len >= r and column_len >= c and graph[r-1][c-1] == k:
        time = i
        break
    
    # 열이 행보다 길면 회전
    if column_len > row_len:
        flag = 1
        graph = rotate_a_matrix_by_90_degree(graph)
        row_len, column_len = column_len, row_len
    
    # 정렬된 배열 삽입
    for x in range(row_len):
        graph[x] = get_new_sorted_array(graph[x])
    
    # 0 채워넣기
    max_len = max([len(row) for row in graph])
    for x in range(row_len):
        fill_len = max_len - len(graph[x])
        graph[x] += [0] * fill_len
    
    if flag:
        graph = rotate_a_matrix_by_90_degree(graph)
    
print(100 if time == -1 and len(graph) >= r and len(graph[0]) >= c and graph[r-1][c-1] == k else time)