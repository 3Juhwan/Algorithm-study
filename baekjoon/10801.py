a = list(map(int, input().split()))
b = list(map(int, input().split()))
cntA, cntB = [0]*2
for x, y in zip(a, b):
    if x == y:
        pass
    elif x > y:
        cntA += 1
    else:
        cntB += 1

if cntA == cntB:
    print('D')
elif cntA > cntB:
    print('A')
else:
    print('B')