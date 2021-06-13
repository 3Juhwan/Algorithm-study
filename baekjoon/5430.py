import sys
input = sys.stdin.readline

def trimString(string):
    string = string[1:-1].split(',')
    if '' in string:
        return list()
    return list(map(int, string))

def joinString(string):
    string = ",".join(map(str, string))
    return "[" + string + "]"

T = int(input())

for _ in range(T):
    p = list(input().rstrip())
    n = int(input())
    arr = input().rstrip()
    arr = trimString(arr)
    
    # mode 0 -> top, mode 1 -> bottom
    top, bottom, mode = 0, 0, 0
    errorCheck = 0
    for command in p:
        if command == "R":
            mode = not mode
        elif command == "D":
            if top + bottom >= n:
                errorCheck = 1
                break
            elif mode:
                bottom += 1
            elif not mode:
                top += 1
    
    # output
    arr = arr[top:n - bottom]
    if errorCheck:
        print("error")
    elif mode:
        result = joinString(arr[::-1])
        print(result)
    else:
        result = joinString(arr)
        print(result)