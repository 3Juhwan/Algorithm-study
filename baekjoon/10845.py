K, N = map(int, input().split())
loop = list(range(1, K+1))
output = []
idx = 0

while len(loop) > 0:
    idx += N
    while idx > len(loop):
        idx -= len(loop)
    output.append(loop.pop(idx-1))
    idx -= 1

print('<', end='')
for i in range(len(output)):
    if i == 0:
        print(output[i], end='')
    else:
        print(',', output[i], end='')
print('>', end='')
