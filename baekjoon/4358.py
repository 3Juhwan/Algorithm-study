import sys
input = sys.stdin.readline

hash = {}
n = 0

while True:
    tree = input().rstrip()
    if not tree:
        break
    hash[tree] = hash[tree] + 1 if tree in hash else 1
    n += 1
    
for key, val in sorted(hash.items()):
    print(key, '%.4f' % round(val*100/n, 4))