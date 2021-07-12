import sys
input = sys.stdin.readline

string1 = list(input().rstrip())
string2 = list(input().rstrip())

arr = [[0] * (len(string2) + 1) for _ in range(len(string1) + 1)]

maxLen = 0
for i in range(1, len(string1) + 1):
    for j in range(1, len(string2) + 1):
        if string1[i-1] == string2[j-1]:
            arr[i][j] = arr[i-1][j-1] + 1
            maxLen = max(maxLen, arr[i][j])

print(maxLen)