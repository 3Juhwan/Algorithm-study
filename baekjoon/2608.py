import sys
input = sys.stdin.readline

s1 = list(input().rstrip())
s2 = list(input().rstrip())

d = {
	'I': 1,
	'V': 5,
	'X': 10,
	'L': 50,
	'C': 100,
	'D': 500,
	'M': 1000,
	'IV': 4,
	'IX': 9,
	'XL': 40, 
	'XC': 90,
	'CD': 400, 
	'CM': 900
}

i = 0
answer1, answer2 = [0] * 2
while i < len(s1)-1:
	tmp = ''.join(s1[i:i+2])
    if tmp in d:
        answer1 += d[tmp]
        i += 2
    else:
        answer1 += d[s1[i]]
        i += 1
if i != len(s1):
	answer1 += d[s1[-1]]
i = 0
while i < len(s2)-1:
	tmp = ''.join(s2[i:i+2])
    if tmp in d:
        answer1 += d[tmp]
        i += 2
    else:
        answer1 += d[s2[i]]
        i += 1
if i != len(s2):
	answer1 += d[s2[-1]]

print(answer1)
for key, value in sorted(d.items(), key=lambda x: x[1], reverse=True):
    while answer1 >= value:
        print(key, end='')
        answer1 -= value