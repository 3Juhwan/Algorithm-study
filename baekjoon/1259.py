while True:
    flag = 1
    n = input()
    if n == '0':
        break

    for i in range(len(n) // 2):
        if n[i] != n[len(n) - i - 1]:
            print('no')
            flag -= 1
            break
    if flag:
        print('yes')
