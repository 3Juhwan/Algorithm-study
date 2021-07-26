import sys
input = sys.stdin.readline
inf = int(1e9)

def NUMX(stack, x):
    stack.append(x)
    return 1

def POP(stack):
    if not stack: return -1
    stack.pop()
    return 1
    
def INV(stack):
    if not stack: return -1
    stack[-1] = -stack[-1]
    return 1
    
def DUP(stack):
    if not stack: return -1
    stack.append(stack[-1])
    return 1
    
def SWP(stack):
    if len(stack) < 2: return -1
    swp = [stack.pop() for _ in range(2)]
    for i in range(2): stack.append(swp[i])
    return 1
    
def ADD(stack):
    if len(stack) < 2: return -1
    stack.append(sum([stack.pop() for _ in range(2)]))
    return 1
    
def SUB(stack):
    if len(stack) < 2: return -1
    x, y = [stack.pop() for _ in range(2)]
    stack.append(y - x)
    return 1
    
def MUL(stack):
    if len(stack) < 2: return -1
    x, y = [stack.pop() for _ in range(2)]
    stack.append(x * y)
    return 1
    
def DIV(stack):
    if len(stack) < 2 or stack[-1] == 0: return -1
    y, x = [stack.pop() for _ in range(2)]
    isPlus = 1 if x * y >= 0 else 0
    result = abs(x) // abs(y)
    if isPlus: stack.append(result)
    else: stack.append(-result)
    return 1
    
def MOD(stack):
    if len(stack) < 2 or stack[-1] == 0: return -1
    y, x = [stack.pop() for _ in range(2)]
    isPlus = 1 if x > 0 else 0
    result = abs(x) % abs(y)
    if isPlus: stack.append(result)
    else: stack.append(-result)
    return 1

while True:
    # 명령어 입력
    commands = []
    command = input().rstrip()
    if command == 'QUIT': break
    while not command == 'END':
        commands.append(command.split())
        command = input().rstrip()
    
    # 입력영역 입력
    n = int(input())
    numbers = [int(input()) for _ in range(n)]
    
    input()
    
    ### 프로그램 실행 ###
    
    for number in numbers:
        goStack = [number]
        isError = 0
        
        for command in commands:
            # NUM
            if len(command) == 2:
                isError = NUMX(goStack, int(command[1]))
            elif command[0] == 'POP':
                isError = POP(goStack)
            elif command[0] == 'INV':
                isError = INV(goStack)
            elif command[0] == 'DUP':
                isError = DUP(goStack)
            elif command[0] == 'SWP':
                isError = SWP(goStack)
            elif command[0] == 'ADD':
                isError = ADD(goStack)
            elif command[0] == 'SUB':
                isError = SUB(goStack)
            elif command[0] == 'MUL':
                isError = MUL(goStack)
            elif command[0] == 'DIV':
                isError = DIV(goStack)
            elif command[0] == 'MOD':
                isError = MOD(goStack)
            
            if isError == -1 or (goStack and abs(goStack[-1]) > inf):
                goStack = []
                break
        
        if len(goStack) == 1: print(goStack[0])
        else: print('ERROR')
        
    print()