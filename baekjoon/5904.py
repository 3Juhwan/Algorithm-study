import sys

n = int(input())

idx, l = 0, 3
while n > l:
    l = l*2+idx+4
    idx += 1


def moomoo(l, i, n):  # l은 길이, i는 수열에서 몇 번째, n은 남은 길이
    t_l = (l-i-3)//2

    if n <= t_l:
        moomoo(t_l, i-1, n)
    elif n <= t_l + i+3:
        n -= t_l
        if n == 1:
            print('m')
        else:
            print('o')
        sys.exit()
    else:
        moomoo(t_l, i-1, n-t_l-i-3)


moomoo(l, idx, n)