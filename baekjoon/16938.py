from itertools import combinations
import sys
input = sys.stdin.readline

N, L, R, X = map(int, input().split())
arr = sorted(list(map(int, input().split())))

result = 0
for i in range(2, N + 1):
    extract = list(combinations(arr, i))
    for x in extract:
        diff = x[-1] - x[0]
        if diff >= X and L <= sum(x) <= R:
            result += 1
    
print(result)