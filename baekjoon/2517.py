from copy import deepcopy
import sys
input = sys.stdin.readline


def merge(left, right):
    i, j = [0] * 2
    sorted_list = []

    while len(left) > i and len(right) > j:
        if left[i] <= right[j]:
            sorted_list.append(right[j])
            cnt[comp[right[j]]] += len(left) - i
            j += 1
        else:
            sorted_list.append(left[i])
            i += 1

    if len(left) > i:
        sorted_list.extend(left[i:])

    if len(right) > j:
        sorted_list.extend(right[j:])
    
    return sorted_list


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left_list = merge_sort(arr[:mid])
    right_list = merge_sort(arr[mid:])

    return merge(left_list, right_list)


n = int(input())
arr = [int(input()) for __ in range(n)]
s = sorted(arr)
comp = {s[i]: i for i in range(len(arr))}
cnt = [0] * len(arr)

merge_sort(arr)

for i, x in enumerate(arr):
    print(i - cnt[comp[x]] + 1)