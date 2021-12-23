def getDivisor(x):
    ret = []
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            ret.append(i)
    ret += list(map(lambda i: x//i, ret))
    return sorted(ret)


def getEulerFn(x):
    ret = x
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            while x % i == 0:
                x //= i
            ret = ret * (i-1) // i
    if x > 1:
        ret = ret * (x-1) // x
    return ret


def solve(n):
    for x in getDivisor(n):
        if x * getEulerFn(x) == n:
            return x
    return -1


n = int(input())
print(solve(n))