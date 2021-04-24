n = int(input())
result = 0

coin_type = [500, 100, 50, 10]

for c in coin_type:
    result += n // c
    n %= c
    
print(result)