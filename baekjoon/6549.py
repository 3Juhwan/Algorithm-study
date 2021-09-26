import sys
input = sys.stdin.readline

while True:
    answer = 0
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    del arr[0]

    q = [(arr[0], 0)]
    for i in range(1, len(arr)):
        idx = i
        while q and q[-1][0] > arr[i]:
            num, idx = q.pop()
            answer = max(answer, num * (i-idx))
        q.append((arr[i], idx))

    while q:
        num, idx = q.pop()
        answer = max(answer, num * (len(arr)-idx))

	print(answer)