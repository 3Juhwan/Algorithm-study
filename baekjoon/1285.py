import sys
input = sys.stdin.readline

n = int(input())
coins = [list(input().rstrip()) for __ in range(n)]
for i in range(n):
    for j in range(n):
        if coins[i][j] == 'H':
            coins[i][j] = '1'
        else:
            coins[i][j] = '0'


def brute_force(idx):
    global answer

    if idx == n:
        return -1

    answer = min(answer, getMaxCoinNum())

    brute_force(idx+1)
    reverseCoins(idx)

    brute_force(idx+1)
    reverseCoins(idx)


def getMaxCoinNum():
    n, cnt = len(coins), 0
    for line in coins:
        tmp = line.count('0')
        cnt += min(tmp, n-tmp)
    return cnt


def reverseCoins(idx):
    for i in range(n):
        coins[i][idx] = '1' if coins[i][idx] == '0' else '0'


answer = 401
brute_force(0)
print(answer)