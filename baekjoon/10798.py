arr = [input() for __ in range(5)]
k = max(map(len, arr))
for i in range(k):
    for j in range(5):
        if len(arr[j]) > i:
            print(arr[j][i], end='')