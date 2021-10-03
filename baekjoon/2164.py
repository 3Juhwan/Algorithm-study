from collections import deque

q = deque(list(range(1, int(input())+1)))
while len(q) > 1:
    q.popleft()
    if len(q) == 1: break
    q.append(q.popleft())
print(q[0])