from collections import deque
import sys
input = sys.stdin.readline

a = list(input().rstrip())
b = list(input().rstrip())
b = deque(b)
flag = 0
while len(a) < len(b):
    if flag:
        if b[-1] == "A":
            b.popleft()
        elif b[-1] == "B":
            b.popleft()
            flag = not flag
    elif not flag:
        if b[-1] == "A":
            b.pop()
        elif b[-1] == "B":
            b.pop()
            flag = not flag
b = list(b)
if flag: b = ''.join(b[::-1])
else: b = ''.join(b)
a = ''.join(a)


if a == b: print(1)
else: print(0)