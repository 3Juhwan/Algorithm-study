a, b, c = map(int, input().split())

def answer(a, b, c):
    if b == 1:
        return a % c
    if b%2 == 0:
        return answer(a, b//2, c)**2 % c
    else:
        return answer(a, b//2, c)**2 * a % c

print(answer(a, b, c))