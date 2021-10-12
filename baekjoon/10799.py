s = []
arr = input()
answer, razer_cnt = [0]*2
for i in range(len(arr)):
    if arr[i] == '(':
        s.append(razer_cnt)
    if arr[i] == ')':
        tmp = s.pop()
        if arr[i-1] == '(':
            razer_cnt += 1
        else:
            answer += razer_cnt - tmp + 1
    if not s:
        razer_cnt = 0
print(answer)