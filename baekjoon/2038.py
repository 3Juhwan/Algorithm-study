def solution(x):
    dp = [0, 1, 2, 2]
    now, total, flag = 3, 5, 3
    
    if x <= 3: return dp[x]
    
    while True:
        for i in range(dp[now]):
            dp.append(now)
            total, flag = total + now, flag + 1
            if total >= x: return flag
        now += 1

n = int(input())
print(solution(n))