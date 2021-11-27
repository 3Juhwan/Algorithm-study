import sys
input = sys.stdin.readline

n = int(input())
k = int(input())


def getCnt(n, x):
    cnt = 0
    for i in range(1, n+1):
        cnt += min(x, n*i)//i
    return cnt


answer = 0
s, e = 0, n**2
while s <= e:
    mid = (s+e)//2
    r = getCnt(n, mid)
    if r >= k:
        answer = mid
        e = mid-1
    else:
        s = mid+1

print(answer)