idx = []

for i in range(1, 6):
    if 'FBI' in input():
        idx.append(i)

if not idx:
    print('HE GOT AWAY!')
for i in idx:
    print(i, end=' ')
