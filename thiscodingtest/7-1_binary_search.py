N = int(input())
com_data = list(map(int, input().split()))
M = int(input())
input_data = list(map(int, input().split()))

com_data.sort()

def binary_search(target):
    start = 0
    end = len(com_data) - 1
    
    while start <= end:
        mid = (start + end) // 2
        
        if com_data[mid] == target:
            return True
        elif com_data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False

for d in input_data:
    if binary_search(d):
        print('yes', end=' ')
    else:
        print('no', end=' ')