n1, n2 = map(str, input().split())
Atotal = 0
Btotal = 0

for i in range(len(n1)):
    Atotal += int(n1[i])

for i in range(len(n2)):
    Btotal += int(n2[i])

print(Atotal*Btotal)
