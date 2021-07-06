from itertools import combinations

while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0: break

    result = list(combinations(arr[1:], 6))
    for x in result:
    print(*x)
    print()