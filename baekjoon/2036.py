import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for __ in range(n)]
arr.sort(reverse=True)

answer = 0
flag = 1

while arr:
	tmp = arr.pop()

    if flag and tmp > 1:
        arr.append(tmp)
        arr.sort()
        flag = 0
        continue

    if tmp <= 0:
        if arr and arr[-1] <= 0:
            ttmp = arr.pop()
            answer += tmp*ttmp
        else:
            answer += tmp
    elif tmp == 1:
        answer += tmp
    else:
        if arr:
            ttmp = arr.pop()
            answer += tmp*ttmp
        else:
            answer += tmp

print(answer)