# Wrong

arr, tmp = [1], list()
stage = 0
target = int(input())

def addNextNum(x):
    s = x * 5
    if s not in arr:
        tmp.append(s)

    s = x * 3
    if s not in arr:
        tmp.append(s)

    s = x * 2
    if s not in arr:
        tmp.append(s)

    s = x + 1
    if s not in arr:
        tmp.append(s)

while True:
    stage += 1
    for x in arr:
        addNextNum(x)
    arr.extend(tmp)

    if target in arr:
        break

print(stage)