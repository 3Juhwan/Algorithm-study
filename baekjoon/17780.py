import sys
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dxy = [(0, 1), (0, -1), (-1, 0), (1, 0)]

def white_space(number, now, next):
    start = chess_map[now[0]][now[1]].index(number)
    
    # change the chess_map
    moving_pieces = chess_map[now[0]][now[1]][start:]
    chess_map[now[0]][now[1]] = chess_map[now[0]][now[1]][:start]
    chess_map[next[0]][next[1]].extend(moving_pieces)
    
    # change the pieces info
    # when piece moves, above all move
    for piece in moving_pieces:
        pieces[piece][0], pieces[piece][1] = next[0], next[1]


def red_space(number, now, next):
    start = chess_map[now[0]][now[1]].index(number)
    
    # change the chess_map
    moving_pieces = chess_map[now[0]][now[1]][start:]
    moving_pieces.reverse()
    chess_map[now[0]][now[1]] = chess_map[now[0]][now[1]][:start]
    chess_map[next[0]][next[1]].extend(moving_pieces)
    
    # chqnge the pieces info
    for piece in moving_pieces:
        pieces[piece][0], pieces[piece][1] = next[0], next[1]
    

def blue_space(number, now, next):
    dx, dy = now[0] - next[0], now[1] - next[1]
    nx, ny = now[0] + dx, now[1] + dy
    
    pieces[number][2] = dxy.index((dx, dy))
    
    if nx < 0 or nx >= n or ny < 0 or ny >= n or graph[nx][ny] == 2:
        return
    elif graph[nx][ny] == 0:
        white_space(number, (now[0], now[1]), (nx, ny))
    elif graph[nx][ny] == 1:
        red_space(number, (now[0], now[1]), (nx, ny))

# move the piece
def move_piece(number, piece):
    # location
    x, y, i = piece
    nx, ny = x + dx[i], y + dy[i]
    
    if nx < 0 or nx >= n or ny < 0 or ny >= n:
        blue_space(number, (x, y), (nx, ny))
    elif graph[nx][ny] == 0:
        white_space(number, (x, y), (nx, ny))
    elif graph[nx][ny] == 1:
        red_space(number, (x, y), (nx, ny))
    elif graph[nx][ny] == 2:
        blue_space(number, (x, y), (nx, ny))
    
# input
n, k = map(int, input().split())
graph = [list(map(int, input().split())) for __ in range(n)]
pieces = [list(map(int, input().split())) for __ in range(k)]
chess_map = [[[] for __ in range(n)] for __ in range(n)]

result = -1

# minus 1 to every pieces location
for i in range(len(pieces)):
    pieces[i][0], pieces[i][1], pieces[i][2] = pieces[i][0] - 1, pieces[i][1] - 1, pieces[i][2] - 1

# set pieces on the chess_map
for i, piece in enumerate(pieces):
    chess_map[piece[0]][piece[1]].append(i)

# run move pieces
for i in range(1, 1001):
    # move the pieces
    for x, piece in enumerate(pieces):
        now_x, now_y = piece[0], piece[1]
        
        # continue if piece is not on the bottom
        if chess_map[now_x][now_y][0] != x:
            continue
        
        move_piece(x, piece)
        
        # if all pieces are on the same space
        for z in range(len(pieces)):
            qx, qy = pieces[z][0], pieces[z][1]
            if len(chess_map[qx][qy]) >= 4:
                print(i)
                sys.exit()

print(result)