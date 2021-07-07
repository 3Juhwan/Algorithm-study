from math import factorial

N, M, K = map(int, input().split())

# 예외 처리
limit = factorial(N + M) // (factorial(N) * factorial(M))
if limit < K:
    print(-1)
else:
    result = ''
    while K > 0 and N >= 1 and M >= 0:
        t = factorial(N - 1 + M) // (factorial(N - 1) * factorial(M))
        if t < K:
            result += 'z'
            M -= 1
            K -= t
        else:
            result += 'a'
            N -= 1

    result += 'a' * N
    result += 'z' * M
    print(result)    