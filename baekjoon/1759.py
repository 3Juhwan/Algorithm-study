import sys
from itertools import combinations
input = sys.stdin.readline

vowel = ['a', 'e', 'i', 'o', 'u']

L, C = map(int, input().split())
arr = sorted(list(input().split()))

arr = list(combinations(arr, L))

for string in arr:
    cnt = 0
    for s in string:
        if s in vowel:
            cnt += 1
    if 1 <= cnt <= (L - 2):
        print(''.join(string))
