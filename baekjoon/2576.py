arr = [int(input()) for __ in range(7)]
arr = [x for x in arr if x%2 == 1]
if not arr:
    print(-1)
else:
    print(sum(arr))
    print(min(arr))