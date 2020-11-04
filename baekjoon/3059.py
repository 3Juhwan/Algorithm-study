n = int(input())

for i in range(n):
    total = 0
    S = input()

    for i in range(65, 91):
        if chr(i) not in S:
            total += i

    print(total)
