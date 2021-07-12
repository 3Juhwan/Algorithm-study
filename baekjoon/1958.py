import sys
input = sys.stdin.readline

string1 = list(input().rstrip())
string2 = list(input().rstrip())
string3 = list(input().rstrip())

dp = [[[0] * (len(string3) + 1) for _ in range(len(string2) + 1)] for _ in range(len(string1) + 1)]

for i in range(1, len(string1) + 1):
    for j in range(1, len(string2) + 1):
        for k in range(1, len(string3) + 1):
            if string1[i-1] == string2[j-1] == string3[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

print(dp[-1][-1][-1])