info = {
    'Adrian': 'ABC',
    'Bruno': 'BABC',
    'Goran': 'CCAABB',
}

cnt_output = []

R = int(input())
answer = input()
most_correct = 0

for idx in info:
    cnt = 0
    for i, j in zip(answer, range(len(answer))):
        if i == info[idx][j % len(info[idx])]:
            cnt += 1
    cnt_output.append(cnt)

print(max(cnt_output))
for i in range(3):
    if cnt_output[i] == max(cnt_output):
        key_list = list(info)
        print(key_list[i])
