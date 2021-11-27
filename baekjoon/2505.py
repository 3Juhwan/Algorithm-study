import sys
input = sys.stdin.readline


def getSection(string):
    s, e = 0, 0
    for i in range(len(string)-1):
        if string[i+1] != i+1:
            s = i+1
            break

    for i in range(s+1, len(string)):
        if string[i] == s:
            e = i
            break

    return (s, e)


def getSection2(string):
    s, e = 0, 0
    for i in range(len(string), 1, -1):
        if string[i-1] != i-1:
            e = i-1
            break

    for i in range(e-1, 0, -1):
        if string[i] == e:
            s = i
            break

    return (s, e)
        

n = int(input())
arr = [0] + list(map(int, input().split()))

tmp = arr[:]
answer = []
for i in range(3):
    if i > 1 and tmp == list(range(len(tmp))): break
    x, y = getSection(tmp)
    if x and y:
        tmp[x:y+1] = tmp[y:x-1:-1]
        answer.append((x, y))
    else:
        answer.append((1, 1))

if len(answer) > 2:
    tmp = arr[:]
    answer = []
    for i in range(2):
        x, y = getSection2(tmp)
        if x and y:
            tmp[x:y+1] = tmp[y:x-1:-1]
            answer.append((x, y))
        else:
            answer.append((1, 1))

for x in answer: print(*x)