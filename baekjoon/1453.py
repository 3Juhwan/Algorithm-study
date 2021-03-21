seats, cnt = [0] * 101, 0

N = int(input())
wants = list(map(int, input().split()))

for w in wants:
    if seats[w]:
        cnt += 1
    else:
        seats[w] = 1

print(cnt)