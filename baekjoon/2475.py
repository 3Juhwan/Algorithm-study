a = list(map(int, input().split()))
b = list(i*i for i in a)
print(sum(b) % 10)
