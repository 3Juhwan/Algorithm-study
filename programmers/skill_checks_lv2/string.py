# 문자열 최대 최소 출력
def solution(s):
    string = list(map(int, s.split(' ')))
    minN = min(string)
    maxN = max(string)
    answer = '' + str(minN) + ' ' + str(maxN)
    return answer