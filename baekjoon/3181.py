ignore_word = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']

sentence = input().split(' ')
output = sentence[0][0]

for word in sentence[1:]:
    if word not in ignore_word:
        output += word[0]

print(output.upper())
