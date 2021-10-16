sieve = [1] * 10001
sieve[0], sieve[1] = [0] * 2
for i in range(2, 10001):
    if sieve[i]:
        n = 2
        while i * n <= 10000:
            sieve[i*n] = 0
            n += 1

m, n = int(input()), int(input())
prime_num = [i for i, x in enumerate(sieve) if x]
answer = [x for x in prime_num if m <= x <= n]
if not answer:
    print(-1)
else:
    print(sum(answer))
    print(answer[0])