import sys
input = sys.stdin.readline

while True:
    # input
    N, A, B = map(int, input().rstrip().split())
    if N == 0:
        break
    
    q = []
    for _ in range(N):
        K, D1, D2 = map(int, input().rstrip().split())
        diff = abs(D1 - D2)
        q.append((diff, K, D1, D2))
    q.sort()

    result = 0
    for _ in range(N):
        dumb, K, D1, D2 = q.pop()

        # A로 가는 경우
        if D1 <= D2:
            # A가 충분한 경우
            if K <= A:
                result += D1 * K
                A -= K
            # A가 부족한 경우
            else:
                # 남아있는 A를 모두 사용
                result += D1 * A
                left = (K - A)
                A = 0
                # 부족한만큼 B를 사용
                result += left * D2
                B -= left
        # B로 가는 경우
        else:
            # B가 충분한 경우
            if K <= B:
                result += D2 * K
                B -= K
            # B가 부족한 경우
            else:
                # 남아있는 B를 모두 사용
                result += D2 * B
                left = (K - B)
                B = 0
                # 부족한만큼 A를 사용
                result += left * D1
                A -= left
    print(result)