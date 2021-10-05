arr = [int(input()) for __ in range(10)]
print(sum(arr)//10)
dic = {}
for x in arr:
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1
arr2 = list(sorted(dic.items(), key=lambda x: x[1], reverse=True))
print(arr2[0][0])