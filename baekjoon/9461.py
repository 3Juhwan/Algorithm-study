T = int(input())
arr = [0] * 101
arr[1], arr[2], arr[3], arr[4], arr[5] = 1, 1, 1, 2, 2 # 처음 0은 인덱스 맞추기 용도

for _ in range(T):
    N = int(input())
    
    for i in range(6, N + 1):
        arr[i] = arr[i - 1] + arr[i - 5]
    
    print(arr[N])