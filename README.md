# 알고리즘 스터디

  

> 공부하려고 만들었습니다.  
> 빨리 취업하고 싶습니다.

  

백준 닉네임 : **`3Juhwan`**  

### 메모

**21-04-24**  
`이것이 코딩 테스트다` 책으로 공부 시작

---

## 21-05-17

- [미래 도시](thiscodingtest/9-1.py)

플로이드 워셜 알고리즘 기본 예제

---

## 21-05-16

- [BOJ 2141](https://www.acmicpc.net/problem/2141) **우체국**

오랜만에 그리디 쉽지 않은 문제였다.  

여러 방법으로 접근했다. 이진 탐색, DP, 그리디,,,

DP로 푸는 건 실패했고, 이진 탐색은 데이터의 양이 많아서 시간 초과 뜰 것이다.  

그리디로 고민했지만, 접근 조차 안되서 다른 분 블로그를 참고했다.  

마을 위치를 기준으로 정렬하고 마을을 하나씩 방문하며 누적된 인구수가 총 인구수의 절반 이상이면 그 마을에 우체국을 세우면 됐다.  

주의할 점은, 총 인구수가 홀수/짝수에 따라 결과가 달라진다.  

항상 그리디는 생각해내기 쉽진 않은데 알고 나면 단순하다..  

- [BOJ 1890](https://www.acmicpc.net/problem/1890) **점프**

DP 간단한 문제였다.  

- [BOJ 1912](https://www.acmicpc.net/problem/1912) **연속합**

DP 간단한 문제다. 오랜만에 풀어서 그런지 여러번 시간 초과 떴다.  
쉬운 DP문제는 점화식만 세우면 끝난다.  

---

## 21-05-15

- [BOJ 2234](https://www.acmicpc.net/problem/2234) **성곽**

dfs/bfs 문제다.  

문제를 처음 접했을 때, 한 칸에 벽이 4개인데 이 정보를 어떻게 저장하지..? 싶었다.  

문제를 더 읽어보니 이진수 비트로 표현하는 걸 보고 소름돋았다.  

문제 풀이 자체는 별 게 없다.  

bfs로 하고 싶었지만, 첨에 dfs로 풀어서 그냥 했다.  

[이 성에 있는 방의 개수]와 [가장 넓은 방의 넓이]를 구하는 건 어렵지 않았다.  

벽의 방향은 digit = [8, 4, 2, 1]의 숫자를 이용해서 구했다.  

```python
digit = [8, 4, 2, 1]

...

for i in range(4):
    num = node - digit[i]
    if num >= 0:
        node = num
        continue

    nx, ny = x + dx[i], y + dy[i]
    if nx >= 0 and nx < N and ny >= 0 and ny < M and not visited[nx][ny]:
        cnt += dfs(nx, ny)
```

문제는 [하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기]였다.  

우선, 어떻게 접근해야 될지 조차 몰랐다.  

다른 분 코드를 참고했는데, 단순하게 성벽을 하나씩 없얘면서 dfs 돌리는 거였다.  

근데 성벽에 어떤 방향에 벽이 있으며, 어떤 벽을 없얘는지 알 방법이 없었다.  

도저히 몰라서 다른 분 코드를 보니까, & 메서드를 사용해서 풀었다.  

> Python 비트 연산

| 연산자 | 기능 | 문법 |
|---|:---:|---:|
| `&` | 비트 AND | `a & b` |
| `\|` | 비트 OR | `a \| b` |
| `^` | 비트 XOR | `a ^ b` |
| `~` | 비트 NOT | `~x` |

만약 북쪽과 서쪽에 벽이 있다면 -> 6(십진수) 0110(이진수)

& 연산자를 사용해서 벽의 유무를 판단하면 간단하게 풀 수 있다.  

오늘도 새로운 걸 배운다,,,  

- [BOJ 1697](https://www.acmicpc.net/problem/1697) **숨바꼭질**

그래프 문제고, 최단 시간을 구하는 문제라 bfs로 풀어야 된다는 건 캐치했다.  

bfs면 queue를 사용할테고,,, 여기서부터 잘못 생각하기 시작했다.  

최단 시간을 한 번 저장하고 계속 갱신될 거라 생각했다.  

queue에 v1, v2, v3를 계속 집어넣을 거고 중복되는 요소가 queue에 들어갈테니까 언젠가 먼저 저장된 시간보다 더 빠른 시간이 갱신되지 않을까...?  

하면서 DP로 풀었지만 틀렸다.  

다른 분 코드를 보니까, 맨 처음 저장된 시간이 최단 시간이라는 걸 가정하고 풀고 있었다.  

가만 생각해보니까, queue를 사용하고 있고 FIFO이니까 처음 저장되는 시간이 최단 시간인 건 당연한 사실,,,  

다른 분 코드를 거의 베끼긴 했지만,  

```python
# 다른 분 코드
visit[p] = 1
if p - 1 >= 0 and visit[p - 1] == 0:
    queue.append([p - 1, d + 1])

# 내 코드
if v1 >= 0 and not visited[v1]:
    queue.append((v1, cnt + 1))
    visited[v1] = 1
```

값을 push하는 동시에 방문 기록을 해줌으로 queue에 중복된 수가 들어가는 경우를 방지했다.  

> PS. 나는 queue을 조회할 때 queue에서 값을 pop한 후에 조회하는데, queue[0][0] 같은 방식으로 단순하게 조회할 수 있다. 습관이 되서 오히려 힘드네,,,  

---

## 21-05-14

- [BOJ 2331](https://www.acmicpc.net/problem/2331) **반복수열**

- [BOJ 11724](https://www.acmicpc.net/problem/11724) **연결 요소의 개수**

dfs/bfs 기본 예제이다. 너무 오랜만이라 그런가,,, 푸는데 시간 좀 걸렸다.  

---

## 21-05-12

- [BOJ 1753](https://www.acmicpc.net/problem/1753) **최단경로**

다익스트라 문제다. 기초 다익스트라 구현을 요구한다.  

---

## 21-05-11

- [BOJ 1802](https://www.acmicpc.net/problem/1802) **종이 접기**

그리디 문제다. 간단해보이지만 그리 쉽지만은 않았다.  

그냥 단순히 입력 값을 중간을 기준으로 정확한 비대칭을 이루면 된다고 생각했다.  

예를 들면, 00011 000001111 01010010101 이 된다고 생각했다.  

하지만 틀렸다~!  

종이를 직접 접어보니까, 중간을 기준으로 비대칭을 이루는 것뿐만 아니라 절반으로 나눠진 것들도 중간을 기준으로 비대칭을 이루고,,,, 무한 반복이다.  

마치, 이진탐색과 병합정렬을 생각나게 하는 그런 문제였다.  

재귀로도 풀 수 있어 보였지만, 기존에 작성한 코드에 반복문만 씌움으로 간단하게 해결했다.  

---

## 21-05-09

- [BOJ 11052](https://www.acmicpc.net/problem/11052) **카드 구매하기**

기본적인 DP 예제와 같은 문제다!  

---

## 21-05-08

- [BOJ 7576](https://www.acmicpc.net/problem/7576) **토마토**

bfs로 간단하게 풀었다. 한 번에 깔끔하게 맞춰서 기분이 좋다.  

최초에 graph를 돌면서 익은 토마토를 queue에 담는다. O(M * N)  

queue에 든 좌표를 상하좌우 탐색하며 전진해 나간다.  

마지막에 graph를 돈다. O(M * N)  

- [BOJ 10451](https://www.acmicpc.net/problem/10451) **순열 사이클**

dfs 문제를 풀었는데, 쉬워서 그런지 dfs라 생각이 들지 않았다.  

재귀이 아닌 반복문으로 해결했다.  

- [BOJ 2225](https://www.acmicpc.net/problem/2225) **합분해**

어떻게 풀어야 될지 1도 모르겠어서 N과 K를 1부터 차례대로 구해보니까 규칙성이 보였다.  

근데 어떤 이유에서 생기는 규칙성인지 모르겠다. 일단 풀긴 풀었지만, 얻어 걸린 문제.  

다른 분 풀이를 찾아봤는데, 다들 비슷했다. 아래 블로그가 가장 잘 설명하고 있다.  

0부터 N까지의 정수를 K개를 이용해 N을 만드는 방법은 0부터 N개까지 k-1개를 이용해 N을 만드는 개수의 합과 같습니다.  

[[Python]2225. 합분해](https://br-brg.tistory.com/18)


- [BOJ 7662](https://www.acmicpc.net/problem/7662) **이중 우선순위 큐**

최대힙과 최소힙 두 개를 사용해서 풀었다.  

처음엔, length 변수로 입출력 되는 데이터의 갯수를 카운트해서 전체 로직을 짰다.  

이 방법은 문제가 있는데, 

```python
I 1
I 2
D 1
D -1
I 3
D -1
> error
```

예외가 있다.  

다른 분 코드를 참고해보니, visited 리스트로 입출력을 제어했다.  

모든 걸 수정했는데도 계속 시간 초과가 떠서 보니 sys.stdin.readline()을 사용해야 한다.  

부족했던 점은, length 변수가 필요하지 않고 오히려 코드가 복잡해진다.  

---

## 21-05-07

- [BOJ 1927](https://www.acmicpc.net/problem/1927) **최소 힙**

힙을 다뤄본 적이 없어서 풀어봤다.  

heapq를 사용해서 풀었는데, 시간 초과 떠서 sys.stdin.readline()도 사용했다.  

- [BOJ 1654](https://www.acmicpc.net/problem/1654) **랜선 자르기**

이전엔 풀지 못했던 문제를 건드려봤다.  

문제를 보자마자 이진 탐색으로 풀어야 한다고 생각했다.  

입력의 범위가 말도 안 되게 컸기 때문! (랜선의 길이는 2^31-1보다 작거나 같은 자연수이다)  

부족했던 점은,,  

left를 0으로 잡아서 mid가 0이 되는 경우를 방지하지 못했다.  

이것 때문에 시간이 오래 걸렸다.  

- [BOJ 1520](https://www.acmicpc.net/problem/1520) **내리막 길**

DP 문제라지만 아무리 봐도 DFS도 사용해서 풀어야 할 것 같았다.  

계속 반복문을 이용한 보텀업 방식으로 DP를 풀어왔기 때문에 이번에도 시도했지만, 번번이 실패했다.  

아예 DFS만으로 풀어서 제출했지만, 시간 초과가 떴다.  

다른 분 코드를 참고해보니, 재귀를 이용해서 dfs와 탑다운 DP로 푸는 거였다.  

python에서 재귀는 제한이 있어서 사용하지 않으려 하는데, 완전히 배제하진 말아야겠다.  

---

## 21-05-05

- [BOJ 10844](https://www.acmicpc.net/problem/10844) **쉬운 계단 수**

기본적인 DP 예제이다.  

나는 1부터 9까지 수에서 앞자리 수를 붙이는 방식으로 풀었다. 전진하는 방식으로.  

> 1 -> 21 -> 321 -> 2321

| N/첫 자리 수 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|:---:|---|
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | 1 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 2 | 1 |
| 3 | 2 | 3 | 4 | 4 | 4 | 4 | 4 | 4 | 3 | 2 |
| 4 | 3 | 6 | 7 | 8 | 8 | 8 | 8 | 7 | 6 | 3 |

앞자리가 1과 9로 갱신될 땐, 예외적인 상황이 발생한다.  

1로 갱신될 때, 이전 0과 2의 값을 더하는데 0의 값을 제대로! 갱신했어야 한다.  

9로 갱신될 땐, 계단 수가 8밖에 없으므로 이전 8의 값을 그대로 더한다.  

- [BOJ 11048](https://www.acmicpc.net/problem/11048) **이동하기**

기본적인 DP 예제랑 같은 방식으로 풀린다.  

[x][y]칸에 있는 사탕에 [x-1][y], [x][y-1], [x-1][y-1]까지의 최댓값을 더하면 된다.  

구현하는 부분에서 부족한 점이 있다.  

나는 좌표 문제가 나오면 DFS에서 사용하는 방식을 이용하는데, 이게 코드를 더 길고 복잡하게 한다.  

```python
# Good
for j in range(1, m + 1):
    dp[i][j] = s[i - 1][j - 1] + max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        
# Not good
dx = [0, -1, -1]
dy = [-1, 0, -1]

for i in range(3):
    nx, ny = x + dx[i], y + dy[i]

    if nx < 0 or ny < 0:
        continue

    dp[x][y] = max(dp[x][y], db[x][y] + dp[nx][ny])
```

- [BOJ 11057](https://www.acmicpc.net/problem/11057) **오르막 수**

DP 문제인데, 아직 적응이 안 된 것 같다.  

뭔가 반복되는 느낌은 오는데, 점화식을 세우는 건 여전히 어려웠다.  

일일이 직접 도식화해보니, 감이 왔다.  

규칙은 다음과 같다.  

| N/끝의 수 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|:---:|---|
| 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
| 2 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |
| 3 | 55 | 45 | 36 | 28 | 21 | 15 | 10 | 6 | 3 | 1 |

10칸짜리 dp 리스트를 만들어서 갱신해주는 방식으로 풀었다.   

- [BOJ 1463](https://www.acmicpc.net/problem/1463) **1로 만들기**

이코테에서 푼 문제랑 같다. DP 기본 문제이기도 해서 풀이는 생략  

- [BOJ 2012](https://www.acmicpc.net/problem/2012) **등수 매기기**

엄청 간단한 그리디 문제다.  

데이터를 입력받아서 sort로 오름차순 정렬하면 끝나는 문제인데, 근데 6번이나 시간 초과가 떴다.  

계수 정렬로도 풀었지만, 도저히 시간 초과를 해결할 수 없어서, 그냥 PyPy3로 제출했다.   

PyPy3가 Python3 보다 빠른 경향이 있다고 한다.  

---

## 21-05-03

- [BOJ 2133](https://www.acmicpc.net/problem/2133) **타일 채우기**

틀림!

---

## 21-05-02

- [BOJ 2579](https://www.acmicpc.net/problem/2579) **계단 오르기**

틀림!  

- [BOJ 9461](https://www.acmicpc.net/problem/9461) **파도반 수열**

DP 문제라고 해서 풀었는데, 단순히 규칙 찾으면 풀리는 문제였다.  

앞으론 DP 문제집을 찾아서 풀어야겠다..  

- [BOJ 9095](https://www.acmicpc.net/problem/9095) **1, 2, 3 더하기**

기초적인 DP 문제로 점화식만 구하면 된다.  

주어진 수는 1, 2, 3 세 가지인데,  

N = (N-1) `+ 1`  
N = (N-2) `+ 2`  
N = (N-3) `+ 3`  

이고, N-1, N-2, N-3이 어떻게 만들어지는지는 신경 쓰지 않아도 된다.  

따라서, N번째 수는 N-1번째 수와 N-2번째 수와 N-3번째 수를 더하면 된다.  

> a(N) = a(N-1) + a(N-2) + a(N-3)  

---

## 21-04-29

- [효율적인 화폐 구성](thiscodingtest/8-4.py)

**아이디어:**  

가치를 기준으로 1원부터 M원까지 만들기 위해 필요한 화폐 개수를 셌다.  

DP문제로서 점화식을 만들고 코드를 짜야 했다.  

d[i] = d[i-k] + 1 (k는 화폐 단위)

**부족한 점:**  

> if문이 여러 개 있어서 코드가 지저분하고 이해하기 어렵다..  

정답 코드에선 인덱스를 범위가 넘어가지 않게 지정해줘서 if문을 걸어줄 필요가 없다.  

> -1로 초기화하는 바람에 코드가 파이썬답지 않다.  

10001로 초기화해서 min함수를 사용해서 깔끔하게 작성할 수 있다.  

> 가치를 기준으로 작성했다. (1원부터 M원까지)  

정답 코드에선 주어진 화폐를 기준으로 작성했다.  

이렇게 할 경우, 가치 순이 아니라 화폐의 배수 순으로 값이 정해지게 되는데,  

이래도 상관 없는 이유가 큰 값이 지정된다고 해도 min 함수로 갱신할 수 있다.  

- [BOJ 10816](https://www.acmicpc.net/problem/10816) **숫자 카드 2**

계수 정렬을 사용해서 풀었다.  

리스트 크기 정하는 게 중요한데, 숫자의 범위는 (-10,000,000 ≤ N ≤ 10,000,000) 이므로 리스트의 크기를 20,000,000으로 지정해서 -10,000,000부터 -1까지는 arr[10,000,001]부터 arr[20,000,000]까지 저장되도록 했다.  

---

## 21-04-28

- [1로 만들기](thiscodingtest/8-1.py)

**아이디어:**  

보텀업 방식으로 풀어보려 했다.  

1부터 시작해서 stage마다 만들어질 수 있는 수를 리스트에 추가했다.  

> Stage 1

arr = [1]

> Stage 2

arr = [1, 2, 3, 5]

> Stage 3

arr = [1, 2, 3, 4, 5, 6, 9, 10, 15, 25]

이 방식은 엄청나게 시간이 걸린다...  

not in 메서드는 O(n)의 시간이,  

while과 for까지 있으니까 큰 입력일수록 시간이 매우 오래 걸린다.  

**부족한 점:**  

풀이에선 재귀함수와 메모리제이션을 이용해서 풀었다.  

다이나믹 문제를 풀 땐, 풀이를 점화식으로 만든 후 재귀 함수로 풀어야겠다,,,  

---

## 21-04-27

- [떡볶이 떡 만들기](thiscodingtest/7-2.py)

**아이디어:**  

절단기의 높이를 기준으로 이진 탐색을 실행하면 된다.  

처음은 0으로 끝은 떡 중에 가장 큰 값으로 지정해서 범위를 좁혀간다.  

**시간 복잡도:**  

우선, 절단기의 높이(H)를 이전 탐색으로 알아내니까 O(log H)의 시간 복잡도를 갖는다.  

이진 탐색마다 떡의 개수(N)만큼 자르니까,  

총 시간 복잡도는 O(N log H)이다.  

  

> 만약, 매번 떡을 절단할 때마다 N개의 떡을 모두 절단하는 게 아니라 이것조차도 이진 탐색으로 푼다면..?  

우선 arr를 오름차순으로 정렬한다.  

이진 탐색으로 높이(H)보다 긴 떡을 찾아낸다. O(log N)  

높이(H)의 값에 영향을 많이 받을 것 같다.  

최선의 경우엔, 높이(H)보다 큰 떡이 없을 수도 있고  

최악의 경우엔, 모든 떡이 높이(H)보다 클 것이다.  

그런데 매번 떡을 절단할 때마다 연산 개수가 천차만별일 것이다.  

오히려 O(log N)의 시간을 들여 탐색까지 해야 하므로 비효율적일 가능성이 높아서,,, 패쓰!


- [부품 찾기](thiscodingtest/7-1_binary_search.py)

**아이디어:**  

매장 내에 있는 부품을 sort 메서드로 오름차순 정렬하고,  

이진 탐색하면 끝나는 문제다!  

**시간 복잡도:**  

sort 메서드는 O(N log N)의 시간 복잡도를 가지고,  

이진 탐색은 M개의 데이터를 O(log N)의 시간 복잡도로 탐색하므로,  

총 시간 복잡도는 O((M + N) log N) 이다..!

---

## 21-04-26

- [두 배열의 원소 교체](thiscodingtest/6-3.py)

**아이디어:**  

리스트 A는 오름차순으로, 리스트 B는 내림차순으로 정렬한다.  

그 후, 처음 원소부터 차례대로 비교해서 B의 원소가 크다면 스왑!  

작다면, 그 이후 원소들도 작을 테니 break!

- [성적이 낮은 순서로 학생 출력하기](thiscodingtest/6-2.py)

**아이디어:**  

수의 범위가 정해져 있어서 계수 정렬로도 풀 수 있지만, 파이썬 sorted에 key를 설정해서 간단하게 풀었다.  

(이름, 점수)를 묶어서 튜플 형태로 리스트에 저장하고 점수를 기준으로 정렬했다.  

- [위에서 아래로](thiscodingtest/6-1.py)

**아이디어:**  

수의 범위가 정해져 있어서 계수 정렬도 효과적으로 쓸 수 있지만, 그냥 sort 함수를 사용해서 풀었다. 

- [미로 탈출](thiscodingtest/5-2_bfs.py)

**아이디어:**

최단 거리 문제는 bfs가 효과적이다..! bfs는 높이 순서대로 방문하기 때문에, 깊이가 무한대라도 탈출 지점까지의 최단 거리는 계산할 수 있다.  

최초의 모든 미로 길에는 1의 값이 저장되어 있다.  
(1, 1)에서 출발해서 이동하는 미로 길엔 이전 노드보다 1이 큰 값이 저장하면 탈출 지점엔 최단 거리가 저장된다.  

정답 코드랑 거의 유사하게 작성해서 뿌듯하다. 

--- 

## 21-04-25

- [음료수 얼려 먹기](thiscodingtest/5-1_bfs.py)  

**아이디어:**

bfs로 구멍이 뚫려 있는 부분을 한 번에 검사하는 방식으로 풀었다.  

**부족한 점:**

풀이는 dfs로 구현되어 있는데, 코드가 훨씬 간결하다.  

예외 처리는 빨리하는 것이 깔끔하다.  

```pythpn
# Good
if nx <= -1 or nx >= N or ny <= -1 or ny >= M:
    continue
if input_data[nx][ny] == 0:
    input_data[nx][ny] = 1
    queue.append((nx, ny))

# Not Good
if nx >= 0 and nx < N and ny >= 0 and ny < M:
    if input_data[nx][ny] == 0:
        queue.append((nx, ny))
        input_data[nx][ny] = 1
```

- [왕실의 나이트](thiscodingtest/4-2.py)  

**시간 복잡도:** O(1)  

**아이디어:** 

이동 경로를 tuple과 list를 이용해서 묶을 수 있다. 
```python
steps = [(-2, -1), (-1, -2), ... ]
```
ord(), chr()
```python
ord('a')  # 97
chr(97)  # a
```

- [게임 개발](thiscodingtest/4-3.py)  

**시간 복잡도:** O(N)  

**부족한 점:** 문제 이해도가 부족해서 의도와 다른 코드를 작성했다. 그래도 뭐,,, 핵심 코드는 얼추 비슷하게 구현해서 일단 넘어가도록 한다.   

**아이디어:**  

이미 지난 곳을 체크할 땐 새로운 list를 만들어서 저장한다. 
```python
d = [[0] * m for _ in range(n)]
```
좌표 문제는 dx, nx 등의 변수명을 사용한다. 
```python
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

nx = x + dx[0]
ny = y + dy[0]
```

--- 

## 21-04-24

- [상하좌우](thiscodingtest/4-1.py)  

**시간 복잡도:** O(N)  

**부족한 점:** 코드가 간결하지 않다. 좌표 문제 풀이 요령을 익힐 필요가 있다. 

- [1이 될 때까지](thiscodingtest/3-4.py)  

**시간 복잡도:** O(N)  

**정당성:** 나눌 수 있으면 무조건 나눠야 한다. 1로 빼는 것보다 K로 나누면 기하급수적으로 수가 감소한다. 

- [숫자 카드 게임](thiscodingtest/3-3.py)  

**시간 복잡도:** O(N^2)  

**아이디어:** 각행마다 가장 작은 수를 뽑고, 그 중 가장 큰 수를 출력 

- [큰 수의 법칙](thiscodingtest/3-2.py)  

**시간 복잡도:** O(N Log N)  

- [거스름돈](thiscodingtest/3-1.py)  

**시간 복잡도:** O(K), K: 화폐 종류  

**정당성:** 화폐 단위가 모두 약수/배수 관계에 있어야 성립한다. 

---

## 21-02-10

- [BOJ 2805](https://www.acmicpc.net/problem/2805) **나무 자르기**   
이진 탐색을 이용하면 쉽게 풀리는 문제였다.

---

## 20-12-10

- [BOJ 2609](https://www.acmicpc.net/problem/2609) **최대공약수와 최소공배수**   

```python
유클리드 호제법 사용하기
```

- [BOJ 11050](https://www.acmicpc.net/problem/11050) **이항계수 1**   

- [BOJ 11866](https://www.acmicpc.net/problem/11866) **요세푸스 문제 0**   
  `list`로 풀었다.  
  근데 보니까 `queue`를 써서 푸는 문제였다.

---

## 20-11-24

- [BOJ 3181](https://www.acmicpc.net/problem/3181) **줄임말 만들기**   

- [BOJ 2839](https://www.acmicpc.net/problem/2839) **설탕배달**   

시간 오래 걸리는 알고리즘으로 풀었다.   

```python
다시 풀어볼 필요가 있다.
```

- [BOJ 1546](https://www.acmicpc.net/problem/1546) **평균**   

- [BOJ 1388](https://www.acmicpc.net/problem/1388) **바닥 장식**   

---

## 20-11-04

- [BOJ 3449](https://www.acmicpc.net/problem/3449) **해밍거리**   

두 문자열을 비교하는 간단한 문제다. 이전에 배운 `zip` 함수를 이용했다.   

- [BOJ 3183](https://www.acmicpc.net/problem/3183) **Dates**   

날짜와 관련된 간단한 문제다. 함수를 만들어 풀었다.   

- [BOJ 3059](https://www.acmicpc.net/problem/3059) **등장하지 않는 문자의 합**   

아스키코드 관련 문자열 문제다. 아스키코드 함수 `chr` 과 `ord` 를 알게 됐다.  

```python
>>> ord('문자') : 아스키코드를 반환
>>> chr('숫자') : 문자 반환
```

- [BOJ 2966](https://www.acmicpc.net/problem/2966) **찍기**   

반복문으로 처리하기 위해 각각의 정보를 `dictionary`로 받았는데,,, 코드가 많이 복잡해졌다.🤣  
`dictionary`보단 `array` 위주로 문제 풀어야겠다.   
[Clean Code](https://alpyrithm.tistory.com/125)

- [BOJ 2857](https://www.acmicpc.net/problem/2857) **FBI**   

이 문제를 풀 때, 사용할 수 있는 함수는 `count` `find` 정도 같다. 물론, 난 사용하지 않았다.

```python
>>> a = "Python is the best choice"
>>> a.find('b')
14
>>> a.find('k')
-1
>>> a.count('e')
33
```

- [BOJ 1259](https://www.acmicpc.net/problem/1259) **팰린드롬수**   

문자열 슬라이싱을 사용하면 매우 간단하게 풀리는 문제였다.  
나는 문자열 슬라이싱에 낯설어서 어렵게 풀었다.

```python
>>> a = 'Hello'
>>> print(a[::-1])
olleH
```

---

## 20-11-03

- [BOJ 1173](https://www.acmicpc.net/problem/1173) **운동**   

문제를 잘 읽어야겠다. 진짜로...   
간단하게 조건문과 반복문으로 풀리는 문제였다.   

- [BOJ 1193](https://www.acmicpc.net/problem/1193) **분수찾기**   

- [BOJ 1225](https://www.acmicpc.net/problem/1225) **이상한곱셈**   

입력받는 수가 최대 10000자리다. 그래서 중첩 반복문을 사용하면 100000000 번의 연산을 해야 하므로 시간초과가 발생한다.  
시간초과를 처음 느껴본 문제이다. 앞으로 런타임도 고려해야겠다.   

- [BOJ 1264](https://www.acmicpc.net/problem/1264) **모음의 개수**   

쉽게 풀었다. 문자열에선 `count` 함수로 특정 문자열이 포함되었는지 확인할 수 있다.   

```python
>> a = 'BlockDMask'
>> print(a.count('k'))
2
```

---

## 20-11-02

- [BOJ 1075](https://www.acmicpc.net/problem/1075) **나누기**   

나는 숫자로 처리했는데, 문자열로 처리하면 더 간단하게 풀 수 있다.   
문자열 처리가 간단해서 파이썬 쓴다는 말을 들은 것 같다.   

- [BOJ 1193](https://www.acmicpc.net/problem/1193) **분수찾기**   

큰 배열에 압도되었지만, 규칙성을 찾으면 아주 쉽게 풀리는 문제다.   

```python
N = input()
F = int(input())

N = int(N[:-2]+'00')

while True:
    if N % F == 0:
        break
    N += 1

print(str(N)[-2:])
```

- [BOJ 1076](https://www.acmicpc.net/problem/1076) **저항**   

어렵게 풀었다는 생각이 많이 든다... 채점하는 데에 120초나 걸리다니..🤣  
`dictionary`로 데이터를 저장하고 풀었는데, 알고보니 데이터에 규칙이 있어서 `list` 하나로도 간단하게 풀 수 있다.   
아직 `python` 으로 문제푸는 스킬이 부족하단 생각이 많이 든다.  

```python
color = ['black', 'brown', 'red',
'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
f = color.index(input())
s = color.index(input())
t = color.index(input())
r = int(str(f) + str(s)) * (10 ** t)
print(r)
```

- [BOJ 1159](https://www.acmicpc.net/problem/1159) **농구경기**   

문자열 슬라이싱으로 괜찮게 풀었다... 고 생각했지만,   
`counter` 라이브러리를 사용하면 쉽게 풀 수 있단 걸 알았다.😥 그래도 꽤 괜찮게 풀었다.   

```python
from collections import Counter
Counter('hello world')
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
```

- [BOJ 10757](https://www.acmicpc.net/problem/10757) **We love kriii**   

- [BOJ 10718](https://www.acmicpc.net/problem/10718) **큰 수 A+B**   

- [BOJ 10869](https://www.acmicpc.net/problem/10869) **사칙연산**   

- [BOJ 10926](https://www.acmicpc.net/problem/10926) **사칙연산**   

- [BOJ 10998](https://www.acmicpc.net/problem/10998) **AxB**   

---

## 20-11-01

- [BOJ 10172](https://www.acmicpc.net/problem/10172) **개**   

`docstring`이라는 문법이 있다. 나중에 알아보도록 하자.

- [BOJ 10430](https://www.acmicpc.net/problem/10430) **나머지**   

- [BOJ 10699](https://www.acmicpc.net/problem/10699) **오늘날짜**   

`time` 라이브러리를 이용해서 풀었다. 지금은 공부하지 않아도 괜찮을 라이브러리라고 생각해서 넘긴다.   

- [BOJ 1453](https://www.acmicpc.net/problem/1453) **피시방알바**   

C언어로 풀었다. 배열 크기를 101로 잡아줘야 한다.   

---

## 20-10-30

- [BOJ 3003](https://www.acmicpc.net/problem/3003) **킹, 퀸, 룩, 비숍, 나이트, 폰**   

절댓값을 적용해야 한다고 생각했지만, 아니었다.  
`list comprehension`에 리스트를 2개 넣어보려고 `zip` 내장함수를 사용해봤다.  
`zip`은 동일한 개수의 자료형을 묶어주는 역할을 하는 함수이다.  

- [BOJ 3046](https://www.acmicpc.net/problem/3046) **R2**   

- [BOJ 5337](https://www.acmicpc.net/problem/5337) **웰컴**   

여러 줄에 걸쳐 출력할 수 있다는 걸 첨 알았다.   

```python
print(""".  .   .
|  | _ | _. _ ._ _  _
|/\|(/.|(_.(_)[ | )(/.""")
```

- [BOJ 5338](https://www.acmicpc.net/problem/5338) **마이크로소프트 로고**   

- [BOJ 5339](https://www.acmicpc.net/problem/5339) **콜센터**   

- [BOJ 5522](https://www.acmicpc.net/problem/5522) **카드게임**   

리스트를 선언해서 풀었는데, 간단하게 변수 하나에 `input`을 더해주는 방식으로도 풀 수 있다.   

- [BOJ 5554](https://www.acmicpc.net/problem/5554) **심부름 가는 길**   

- [BOJ 6749](https://www.acmicpc.net/problem/6749) **Next in line**   

- [BOJ 7287](https://www.acmicpc.net/problem/7287) **등록**   

- [BOJ 8370](https://www.acmicpc.net/problem/8370) **Plane**   

- [BOJ 8393](https://www.acmicpc.net/problem/8393) **합**   

- [BOJ 8437](https://www.acmicpc.net/problem/8437) **julka**   

- [BOJ 9654](https://www.acmicpc.net/problem/9654) **나무함대 데이터**   

`format`과 함께 출력 형식을 제한한 하는 코드를 써봤다.  

```python
>> print('Python is [{:15}]'.format('good'))
python is [good           ]
```

- [BOJ 10170](https://www.acmicpc.net/problem/10170) **NFC West vs North**   
  출력 형식은 어차피 나중에 구글링하면 되니까.. 그냥 `print`문으로 간단하게 처리했다.  

- [BOJ 10171](https://www.acmicpc.net/problem/10171) **고양이**   

---

## 20-10-29

- [BOJ 1550](https://www.acmicpc.net/problem/1550) **16진수**   

아직도 어떤 문제인지 모르겠다.   
다른 분 코드를 보니 한 줄로 처리되는데, 그걸 보고도 문제 파악이 안된다.   
그래도 `int` 함수의 인자로 진법 변환할 수 있단 걸 알았다.   

```python
# int를 이용한 진법 변환
print(int(input(), 16))
```

- [BOJ 2338](https://www.acmicpc.net/problem/2338) **긴자리계산**   

단순 계산 문제이다.   
새로 배운 건, `print` 함수의 두번째 인자로 `sep='\n'`를 주면, 각 줄에 개행을 넣을 수 있다는 것이다.  

```python
>> print(1, 2, sep='\n')
1
2
```

- [BOJ 2475](https://www.acmicpc.net/problem/2475) **검증수**   

아주 간단한 문제이다.   
`map` 함수로 `input`을 받고, `list comprehension` 문법으로 제곱수 배열을 새로 만들었다.  

- [BOJ 2557](https://www.acmicpc.net/problem/2557) **Hello World**   

- [BOJ 2558](https://www.acmicpc.net/problem/2558) **A+B-2**   

- [BOJ 2845](https://www.acmicpc.net/problem/2845) **파티가끝나고난뒤에**   

간단한 문제이다. `map`과 `list comprehension`에 익숙해지기 위해 사용해서 풀어봤다.  

- [BOJ 2914](https://www.acmicpc.net/problem/2914) **저작권**   

`math` 라이브러리를 `import`해서 `ceil`이라는 올림 함수를 사용해봤다.

---

## 20-10-28

- [BOJ 1000](https://www.acmicpc.net/problem/1000) **덧셈**   

아주 간단한 문제지만, 한 줄에 숫자 여러개 받는 방법을 몰랐다.   
`split()` 함수를 이용하면 `()` 사이에 값을 구분자로 하여 문자열로 나누어 준다.   

```python
# split 함수 예시
>>> a = "Life is too short"
>>> a.split()
['Life', 'is', 'too', 'short']
```

- [BOJ 1001](https://www.acmicpc.net/problem/1001) **뺄셈**   

[BOJ 1000](https://www.acmicpc.net/problem/1000) 와 동일한 문제지만 `int()`로 바로 감싸서 풀었다.

- [BOJ 1271](https://www.acmicpc.net/problem/1271) **엄청난 부자2**   

몫과 나머지의 연산자만 사용하면 아주 간단한 문제였다.   
다른 분의 코드를 보니, `map()`함수를 사용하면 더 간단하게 숫자를 받을 수 있단 걸 알았다.   

```python
# map을 이용한 숫자 입력 예제
n, m = map(int, input().split())
```

---
