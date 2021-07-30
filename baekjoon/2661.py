import sys
sys.setrecursionlimit(200000)

def valify(s):
    s_len = len(s)
    for i in range(1, s_len // 2 + 1):
        if s[s_len-i:] == s[s_len-2*i:s_len-i]:
            return 0
    return 1
    
def dfs(s):
    if len(s) == n:
        print(s)
        sys.exit()
    
    for i in range(1, 4):
        if valify(s + str(i)):
            dfs(s + str(i))

n = int(input())
dfs('')