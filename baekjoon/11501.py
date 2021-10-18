import sys
input = sys.stdin.readline


def getMaxBenefit(arr):
    i, answer = [0]*2
    for x in reversed(arr):
        if x > i:
            i = x
        else:
            answer += i-x
    return answer


t = int(input())
for __ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(getMaxBenefit(arr))