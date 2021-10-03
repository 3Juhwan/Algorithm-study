n = int(input())
s1 = list(input().rstrip())
answer = 0
for __ in range(n-1):
    s2 = list(input().rstrip())
    v1, v2 = [0] * len(s1), [0] * len(s2)

    for i in range(len(s1)):
        for j in range(len(s2)):
            if not v1[i] and not v2[j] and s1[i] == s2[j]:
                v1[i], v2[j] = [1] * 2

    b1, b2 = len(s1)-sum(v1), len(s2)-sum(v2)
    if b1 > 1 or b2 > 1:
        continue
    else:
        answer += 1
print(answer)