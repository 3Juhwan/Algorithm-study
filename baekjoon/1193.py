X = int(input())
i = 1

while X > i:
    X -= i
    i += 1

if i % 2 == 1:
    print('%d/%d' % (i+1-X, X))
else:
    print('%d/%d' % (X, i+1-X))
