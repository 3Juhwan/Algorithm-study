N = int(input())
input_data = []

for _ in range(N):
    input_data.append(int(input()))

input_data.sort(reverse=True)

for i in input_data:
    print(i, end=' ')