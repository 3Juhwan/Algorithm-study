papers = [0] + [int(input()) for __ in range(6)]

# 6
answer = papers[6]

# 5
answer += papers[5]
papers[1] -= papers[5] * 11
papers = [x if x > 0 else 0 for x in papers]

# 4
answer += papers[4]
if papers[2] >= papers[4] * 5:
    papers[2] -= papers[4] * 5
else:
    papers[1] -= (papers[4] * 5 - papers[2]) * 4
    papers[2] = 0
papers = [x if x > 0 else 0 for x in papers]

# 3
left = papers[3] // 4
left += 1 if papers[3] % 4 else 0
answer += left
n = 4 - papers[3] % 4
if n == 4:
    pass
elif n == 3:
    if papers[2] >= 5:
        papers[2] -= 5
        papers[1] -= 7
    else:
        left = 7 + (5 - papers[2]) * 4
        papers[2] -= 5
        papers[1] -= left
elif n == 2:
    if papers[2] >= 3:
        papers[2] -= 3
        papers[1] -= 6
    else:
        left = 6 + (3 - papers[2]) * 4
        papers[2] -= 3
        papers[1] -= left
elif n == 1:
    if papers[2] >= 1:
        papers[2] -= 1
        papers[1] -= 5
    else:
        left = 5 + (1 - papers[2]) * 4
        papers[2] -= 1
        papers[1] -= left
papers = [x if x > 0 else 0 for x in papers]

# 2
if papers[2] > 0:
    left = papers[2] // 9
    left += 1 if papers[2] % 9 else 0
    answer += left
    n = 36 - papers[2] % 9 * 4
    if n == 36:
        pass
    else:
        papers[1] -= n
papers = [x if x > 0 else 0 for x in papers]

# 1
if papers[1] > 0:
    answer += papers[1] // 36
    answer += 1 if papers[1] % 36 else 0

print(answer)