T = int(input())

for _ in range(T):
    N = int(input())
    visited = [False for _ in range(N + 1)]
    db = [0] + (list(map(int, input().split())))

    result = 0
    for i in range(1, N + 1):
        if visited[i]:
            continue

        x = i
        while not visited[x]:
            visited[x] = True
            x = db[x]
        result += 1

    print(result)