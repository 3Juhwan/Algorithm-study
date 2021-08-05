import sys
input = sys.stdin.readline

string1 = input().rstrip()
string2 = input().rstrip()

len1 = len(string1)
len2 = len(string2)

dp = [[0] * (len2+1) for _ in range(len1+1)]

for i in range(1, len1+1):
    for j in range(1, len2+1):
        if string1[i-1] == string2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])

result = []
x, y = len1, len2
while x > 0 and y > 0:
    if dp[x-1][y] == dp[x][y]:
        x -= 1
    elif dp[x][y-1] == dp[x][y]:
        y -= 1
    else:
        result.append(string1[x-1])
        x, y = x - 1, y - 1

for s in reversed(result):
    print(s, end='')