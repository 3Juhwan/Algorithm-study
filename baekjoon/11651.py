n = int(input())
location = []

for i in range(n):
    spot = list(map(int, input().split()))
    location.append(spot)

location.sort(key=lambda x:(x[1], x[0]))

for spot in location:
    print(spot[0], spot[1])
