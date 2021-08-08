import sys
input = sys.stdin.readline

n = int(input())
words = [list(input().rstrip()) for __ in range(n)]
dp = [0] * 26
visited = [0] * 26

for word in words:
    visited[ord(word[0])-ord('A')] = 1
    weight = len(word) - 1
    
    for w in word:
        dp[ord(w)-ord('A')] += 10 ** weight
        weight -= 1

ll = len([x for x in dp if x])


if ll > 9:
    arr = [(num, x) for x, num in enumerate(dp)]
    arr.sort()
    for x in arr:
        if not visited[x[1]] and x[0]:
            dp[x[1]] = 0
            break

dp.sort(reverse=True)

result = 0
for i in range(9):
    result += dp[i] * (9 - i)
    
print(result)