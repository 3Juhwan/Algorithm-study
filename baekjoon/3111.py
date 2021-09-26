from collections import deque
import sys
input = sys.stdin.readline

a = list(input().rstrip())
t = deque(list(input().rstrip()))

s, e = 0, len(t) - 1
f_stack, b_stack = [], []
r_a = a[::-1]

while s <= e:
    while s <= e:
        f_stack.append(t[s])
        s += 1
        if len(f_stack) >= len(a) and f_stack[-len(a):] == a:
            f_stack[-len(a):] = []
            break

    while s <= e:
        b_stack.append(t[e])
        e -= 1
        if len(b_stack) >= len(a) and b_stack[-len(a)::] == r_a:
            b_stack[-len(a):] = []
            break

t = deque(f_stack + b_stack[::-1])
stack = []
while t:
    stack.append(t.popleft())
    if len(stack) >= len(a) and stack[-len(a):] == a:
        stack[-len(a):] = []

print(''.join(stack))