n = int(input())

score = list(map(int, input().split()))
maxNum = max(score)
score = [i/maxNum*100 for i in score]

avg = sum(score)/len(score)
print(avg)
