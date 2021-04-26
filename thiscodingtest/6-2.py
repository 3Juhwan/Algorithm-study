N = int(input())
input_data = []
for _ in range(N):
    name, score = input().split()
    score = int(score)
    input_data.append((name, score))

input_data = sorted(input_data, key=lambda student: student[1])

for student in input_data:
    print(student[0], end=' ')