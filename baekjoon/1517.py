import sys
input = sys.stdin.readline

answer = 0

def merge(left, right):
    global answer

    i, j = [0] * 2
    sorted_list = []

    while len(left) > i and len(right) > j:
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
            answer += len(left) - i

    if len(left) > i:
        sorted_list.extend(left[i:])

    if len(right) > j:
        sorted_list.extend(right[j:])

    return sorted_list


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_list = merge_sort(arr[:mid])
    right_list = merge_sort(arr[mid:])
    
    return merge(left_list, right_list)

n = int(input())
arr = list(map(int, input().split()))
merge_sort(arr)
print(answer)