# N = int(input())
# F = int(input())
# cnt = 0

# for i in range(100):
#     N = N // 100 * 100 + i
#     cnt = i

#     if N % F == 0:
#         break

# print('%02d' % cnt)

N = input()
F = int(input())

N = int(N[:-2]+'00')

while True:
    if N % F == 0:
        break
    N += 1

print(str(N)[-2:])
