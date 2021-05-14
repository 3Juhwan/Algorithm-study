visited = [0 for _ in range(236197)]
A, P = map(int, input().split())

def seq(N, P):
    result = 0
    while N > 0:
        val = N % 10
        result += val ** P
        N //= 10
    return result

stack = [A]
visited[A] = 1
x = seq(A, P)
while not visited[x]:
    visited[x] = 1
    stack.append(x)
    x = seq(x, P)

cnt = 0
for i in stack:
    if i == x:
        break
    cnt += 1

print(cnt)