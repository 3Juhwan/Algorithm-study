val = {
    'black': '0',
    'brown': '1',
    'red': '2',
    'orange': '3',
    'yellow': '4',
    'green': '5',
    'blue': '6',
    'violet': '7',
    'grey': '8',
    'white': '9',
}

mul = {
    'black': '',
    'brown': '0',
    'red': '00',
    'orange': '000',
    'yellow': '0000',
    'green': '00000',
    'blue': '000000',
    'violet': '0000000',
    'grey': '00000000',
    'white': '000000000',
}

color = []
total = ''

for i in range(3):
    color.append(input())

for i in range(2):
    total += val[color[i]]
total += mul[color[2]]

print(int(total))
