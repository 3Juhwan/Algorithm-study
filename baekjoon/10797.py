n = int(input())
cnt = [x for x in map(int, input().split()) if x%10 == n]
print(len(cnt))