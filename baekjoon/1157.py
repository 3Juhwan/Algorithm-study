string = input()
string = string.upper()
dp = [0] * 26
for s in list(string):
    n = ord(s) - ord('A')
    dp[n] += 1
m = max(dp)
answer = []
for i, x in enumerate(dp):
    if x == m:
        answer.append(i)
if len(answer) >= 2:
    print('?')
else:
    print(chr(answer[0]+ord('A')))