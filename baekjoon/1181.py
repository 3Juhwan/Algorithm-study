N = int(input())
words = []
for i in range(N):
    word = input()
    if word not in words:
        words.append(word)

words.sort(key=lambda x:(len(x), x))

for i in words:
    print(i)
