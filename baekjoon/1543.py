import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()
answer = 0
i = 0
while i <= len(a) - len(b):
    if a[i:i+len(b)] == b:
        answer += 1
        i += len(b)
    else:
        i += 1

print(answer)