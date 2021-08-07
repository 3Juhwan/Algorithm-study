import sys
input = sys.stdin.readline

def get_candidate(x, y):
    nums = [0] + [1] * 9
    
    nx, ny = x // 3 * 3, y // 3 * 3
    for i in range(nx, nx + 3):
        for j in range(ny, ny + 3):
            num = int(graph[i][j])
            nums[num] = 0
            
    for i in range(9):
        num = int(graph[i][y])
        nums[num] = 0
        num = int(graph[x][i])
        nums[num] = 0
    
    return [i for i, e in enumerate(nums) if e]
    
def dfs():
    if not empty_list:
        for row in graph:
            print(''.join(row))
        sys.exit()
    
    x, y = empty_list.pop()

    # 입력 가능한 문자열
    possible_list = get_candidate(x, y)

    for i in possible_list:
        graph[x][y] = str(i)
        dfs()
    
    graph[x][y] = '0'
    empty_list.append((x, y))

graph = [list(input().rstrip()) for _ in range(9)]

empty_list = [(i, j) for i in range(9) for j in range(9) if graph[i][j] == '0']

empty_list.reverse()

dfs()