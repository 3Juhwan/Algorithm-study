import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
a, b = map(int, input().split())

arr = [x-a for x in arr if x > a]
answer = [x//b+1 if x % b else x//b for x in arr]
print(sum(answer) + n)