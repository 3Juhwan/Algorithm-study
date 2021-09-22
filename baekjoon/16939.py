import sys
from copy import deepcopy
input = sys.stdin.readline


def rotate_clck(v):
	return [v[2], v[0], v[3], v[1]]

	
def rotate_a_clck(v):
	return [v[1], v[3], v[0], v[2]]


def check_cube(cube):
    for v in cube:
        if max(v) != min(v):
            return 0
	return 1

cube = []

arr = list(map(int, input().split()))
for i in range(0, 24, 4):
	cube.append(arr[i:i+4])

answer = 0

# 좌측 뒤로 회전
n_cube = deepcopy(cube)
n_cube[0][0], n_cube[0][2], n_cube[1][0], n_cube[1][2], n_cube[2][0], n_cube[2][2], n_cube[5][3], n_cube[5][1] = cube[1][0], cube[1][2], cube[2][0], cube[2][2], cube[5][3], cube[5][1], cube[0][0], cube[0][2]
n_cube[3] = rotate_a_clck(cube[3])
answer += check_cube(n_cube)

# 좌측 앞으로 회전
n_cube = deepcopy(cube)
n_cube[0][0], n_cube[0][2], n_cube[1][0], n_cube[1][2], n_cube[2][0], n_cube[2][2], n_cube[5][3], n_cube[5][1] = cube[5][3], cube[5][1], cube[0][0], cube[0][2], cube[1][0], cube[1][2], cube[2][0], cube[2][2]
n_cube[3] = rotate_clck(cube[3])
answer += check_cube(n_cube)

# 위측 시계 회전
n_cube = deepcopy(cube)
n_cube[3][0], n_cube[3][1], n_cube[1][0], n_cube[1][1], n_cube[4][0], n_cube[4][1], n_cube[5][0], n_cube[5][1] = cube[1][0], cube[1][1], cube[4][0], cube[4][1], cube[5][0], cube[5][1], cube[3][0], cube[3][1]
n_cube[0] = rotate_clck(cube[0])
answer += check_cube(n_cube)

# 위측 반시계 회전
n_cube = deepcopy(cube)
n_cube[3][0], n_cube[3][1], n_cube[1][0], n_cube[1][1], n_cube[4][0], n_cube[4][1], n_cube[5][0], n_cube[5][1] = cube[5][0], cube[5][1], cube[3][0], cube[3][1], cube[1][0], cube[1][1], cube[4][0], cube[4][1]
n_cube[0] = rotate_a_clck(cube[0])
answer += check_cube(n_cube)

# 앞측 시계 회전
n_cube = deepcopy(cube)
n_cube[0][2], n_cube[0][3], n_cube[4][0], n_cube[4][2], n_cube[2][1], n_cube[2][0], n_cube[3][3], n_cube[3][1] = cube[3][3], cube[3][1], cube[0][2], cube[0][3], cube[4][0], cube[4][2], cube[2][1], cube[2][0]
n_cube[1] = rotate_clck(cube[1])
answer += check_cube(n_cube)

# 앞측 반시계 회전
n_cube = deepcopy(cube)
n_cube[0][2], n_cube[0][3], n_cube[4][0], n_cube[4][2], n_cube[2][1], n_cube[2][0], n_cube[3][3], n_cube[3][1] = cube[4][0], cube[4][2], cube[2][1], cube[2][0], cube[3][3], cube[3][1], cube[0][2], cube[0][3]
n_cube[1] = rotate_a_clck(cube[1])
answer += check_cube(n_cube)

print(1 if answer else 0)
