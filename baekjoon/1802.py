T = int(input())

for _ in range(T):
    flag = 1
    arr = list(input())
    length = len(arr)
    
    while length > 1:
        for i in range(length // 2):
            if arr[i] != arr[length - i - 1]:
                continue
            flag = 0
        length //= 2
        
    print("YES" if flag else "NO")