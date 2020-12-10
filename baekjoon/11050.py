def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


N, K = map(int, input().split())
output = int(factorial(N)/factorial(K)/factorial(N-K))

print(output)
