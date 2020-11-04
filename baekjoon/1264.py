a = []
vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

sentence = input()
while sentence != '#':
    cnt = 0
    for i in sentence:
        if i in vowel:
            cnt += 1
    a.append(cnt)

    sentence = input()

for i in a:
    print(i)
