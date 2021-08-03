def ttClock(a):
    f1, f2, f3 = a[0], a[1], a[2]
    f1[0], f1[1], f1[2], f2[0], f2[2], f3[0], f3[1], f3[2] = f3[0], f2[0], f1[0], f3[1], f1[1], f3[2], f2[2], f1[2]
    
def ttCClock(a):
    ttClock(a)
    ttClock(a)
    ttClock(a)

def turnFrontSidesClockwise():
    cube[0][2], cube[2][2], cube[5][2], cube[4][2] = cube[4][2], cube[0][2], cube[2][2], cube[5][2]

def turnFrontSidesCounterClockwise():
    cube[0][2], cube[2][2], cube[5][2], cube[4][2] = cube[2][2], cube[5][2], cube[4][2], cube[0][2]

def turn(x):
    if x == '+':
        ttClock(cube[1])
        turnFrontSidesClockwise()
        
    else:
        ttCClock(cube[1])
        turnFrontSidesCounterClockwise()
        
    
def moveLeft():
    cube[1], cube[2], cube[3], cube[4] = cube[4], cube[1], cube[2], cube[3]
    ttCClock(cube[0])
    ttCClock(cube[1])
    ttCClock(cube[2])
    ttClock(cube[3])
    ttClock(cube[4])
    ttClock(cube[5])
    
def moveRight():
    cube[1], cube[2], cube[3], cube[4] = cube[2], cube[3], cube[4], cube[1]
    ttClock(cube[0])
    ttClock(cube[1])
    ttCClock(cube[2])
    ttCClock(cube[3])
    ttClock(cube[4])
    ttCClock(cube[5])
    
def moveUp():
    cube[0], cube[1], cube[5], cube[3] = cube[1], cube[5], cube[3], cube[0]
    for _ in range(2): ttClock(cube[1])
    for _ in range(2): ttClock(cube[3])
    ttCClock(cube[4])
    ttClock(cube[2])

def moveDown():
    cube[0], cube[1], cube[5], cube[3] = cube[3], cube[0], cube[1], cube[5]
    for _ in range(2): ttClock(cube[0])
    for _ in range(2): ttClock(cube[5])
    ttCClock(cube[2])
    ttClock(cube[4])

def printCube():
    for upSide in cube[0]:
        for up in upSide:
            print(up, end='')
        print()

t = int(input())
for _ in range(t):
    cube = [
        [['w'] * 3 for _ in range(3)],    # 윗면
        [['r'] * 3 for _ in range(3)],    # 정면
        [['b'] * 3 for _ in range(3)],    # 오른면
        [['o'] * 3 for _ in range(3)],    # 뒷면
        [['g'] * 3 for _ in range(3)],    # 왼쪽면
        [['y'] * 3 for _ in range(3)],    # 아랫면
    ]
    
    n = int(input())
    commands = list(input().rstrip().split())
    
    for command in commands:
        turnSide, turnDirection = command[0], command[1]
        
        if turnSide == 'U':
            moveDown()
            turn(turnDirection)
            moveUp()
        elif turnSide == 'D':
            moveUp()
            turn(turnDirection)
            moveDown()
        elif turnSide == 'F':
            turn(turnDirection)
        elif turnSide == 'B':
            for _ in range(2): moveLeft()
            turn(turnDirection)
            for _ in range(2): moveRight()
        elif turnSide == 'R':
            moveRight()
            turn(turnDirection)
            moveLeft()
        elif turnSide == 'L':
            moveLeft()
            turn(turnDirection)
            moveRight()
    printCube()