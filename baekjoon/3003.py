ipt = list(map(int, input().split()))
weight = [1, 1, 2, 2, 2, 8]

ipt = [(j-i) for i, j in zip(ipt, weight)]

for i in ipt:
    print(i, end=' ')
