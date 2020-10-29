# 저작권 멜로디 / 곡의 개수 => 올림 = 평균
# (평균 -0.51) * 곡의 개수
import math
music_n, avg = map(int, input().split())
print(math.ceil((avg-0.99)*music_n))
