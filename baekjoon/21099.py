n = int(input())
ar = list(map(int, input().split()))
answer = 0
if n*(n-1)//2 > (1<<17):
    answer = 1
else:
    dp = [0] * ((1<<17)+1)
    for i in range(n-1):
        for j in range(i+1, n):
            if ar[i] != ar[j]:
                re = ar[i]^ar[j]
                if dp[re]:
                    answer = 1
                dp[re] = 1
print('Yes' if answer else 'No')