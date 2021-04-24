N = int(input())
guide = list(map(str, input().split()))

x, y = 1, 1

for g in guide:
    if g == 'L' and x > 1:
        x -= 1
    elif g == 'R' and x < N:
        x += 1
    elif g == 'U' and y > 1:
        y -= 1
    elif g == 'D' and y < N:
        y += 1

print(x, y)
