data = input()

result = 0
x = int(ord(data[0]) - ord('a')) + 1
y = int(data[1])

dx = [-2, -1, -2, -1, 1, 2, 2, 1]
dy = [-1, -2, 1, 2, -2, -1, 1, 2]

for i in range(8):
    nx, ny = x + dx[i], y + dy[i]
    
    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        result += 1
        
print(result)