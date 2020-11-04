n = int(input())

for i in range(n):
    n1, n2 = input(), input()
    cnt = 0

    for i, j in zip(n1, n2):
        if i != j:
            cnt += 1
    print('Hamming distance is %d.' % cnt)
