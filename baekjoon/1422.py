k, n = map(int, input().split())
arr = [input() for __ in range(k)]
arr += [str(max(map(int, arr)))*(n-k)]
arr.sort(key=lambda x: (x*50)[:50], reverse=True)
print(''.join(arr))