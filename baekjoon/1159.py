N = int(input())
name_list = []
permit = []
tcnt = 0

for i in range(N):
    name_list.append(input())

for i in range(N-1):
    tmp = name_list[i][0]
    if tmp in permit:
        continue
    cnt = 0

    for j in range(i, N):
        if name_list[j][0] == tmp:
            cnt += 1
    if cnt >= 5 and tmp not in permit:
        permit.append(tmp)
        tcnt += 1

permit.sort()

if tcnt == 0:
    print('PREDAJA')
else:
    for i in permit:
        print(i, end='')
