# 알고리즘 스터디

<br />

> 공부하려고 만들었습니다.  
> 빨리 취업하고 싶습니다.

<br/>

백준 닉네임 : **`3Juhwan`**<br/>

### 메모

**20-10-28**  
공부 시작! 🔥🔥  
하루에 3문제 이상 풀면서 감 잡기!!

**20-11-02**  
한 주 단위로 틀린&수정한 문제 다시 풀기😊  
브론즈 5는 나에게 쉬워서 오늘부터 브론즈 2로 난이도를 높여서 진행한다.

**20-12-10**  
`solve.ac`의 `CLASS 2` 풀기 시작~!

---

## 21-02-10

- [BOJ 2805](https://www.acmicpc.net/problem/2805) **나무 자르기** <br/>
이진 탐색을 이용하면 쉽게 풀리는 문제였다.

---

## 20-12-10

- [BOJ 2609](https://www.acmicpc.net/problem/2609) **최대공약수와 최소공배수** <br/>

```python
유클리드 호제법 사용하기
```

- [BOJ 11050](https://www.acmicpc.net/problem/11050) **이항계수 1** <br/>

- [BOJ 11866](https://www.acmicpc.net/problem/11866) **요세푸스 문제 0** <br/>
  `list`로 풀었다.  
  근데 보니까 `queue`를 써서 푸는 문제였다.

---

## 20-11-24

- [BOJ 3181](https://www.acmicpc.net/problem/3181) **줄임말 만들기** <br/>

- [BOJ 2839](https://www.acmicpc.net/problem/2839) **설탕배달** <br/>

시간 오래 걸리는 알고리즘으로 풀었다. <Br/>

```python
다시 풀어볼 필요가 있다.
```

- [BOJ 1546](https://www.acmicpc.net/problem/1546) **평균** <br/>

- [BOJ 1388](https://www.acmicpc.net/problem/1388) **바닥 장식** <br/>

---

## 20-11-04

- [BOJ 3449](https://www.acmicpc.net/problem/3449) **해밍거리** <br/>

두 문자열을 비교하는 간단한 문제다. 이전에 배운 `zip` 함수를 이용했다. <br/>

- [BOJ 3183](https://www.acmicpc.net/problem/3183) **Dates** <br/>

날짜와 관련된 간단한 문제다. 함수를 만들어 풀었다. <br/>

- [BOJ 3059](https://www.acmicpc.net/problem/3059) **등장하지 않는 문자의 합** <br/>

아스키코드 관련 문자열 문제다. 아스키코드 함수 `chr` 과 `ord` 를 알게 됐다.<br/>

```python
>>> ord('문자') : 아스키코드를 반환
>>> chr('숫자') : 문자 반환
```

- [BOJ 2966](https://www.acmicpc.net/problem/2966) **찍기** <br/>

반복문으로 처리하기 위해 각각의 정보를 `dictionary`로 받았는데,,, 코드가 많이 복잡해졌다.🤣<br/>
`dictionary`보단 `array` 위주로 문제 풀어야 겠다. <br/>
[Clean Code](https://alpyrithm.tistory.com/125)

- [BOJ 2857](https://www.acmicpc.net/problem/2857) **FBI** <br/>

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

- [BOJ 1259](https://www.acmicpc.net/problem/1259) **팰린드롬수** <br/>

문자열 슬라이싱을 사용하면 매우 간단하게 풀리는 문제였다.<br/>
나는 문자열 슬라이싱에 낯설어서 어렵게 풀었다.

```python
>>> a = 'Hello'
>>> print(a[::-1])
olleH
```

---

## 20-11-03

- [BOJ 1173](https://www.acmicpc.net/problem/1173) **운동** <br/>

문제를 잘 읽어야 겠다. 진짜로... <br/>
간단하게 조건문과 반복문으로 풀리는 문제였다. <br/>

- [BOJ 1193](https://www.acmicpc.net/problem/1193) **분수찾기** <br/>

- [BOJ 1225](https://www.acmicpc.net/problem/1225) **이상한곱셈** <br/>

입력 받는 수가 최대 10000자리다. 그래서 중첩 반복문을 사용하면 100000000 번의 연산을 해야 하기 때문에 시간초과가 발생한다.<br/>
시간초과를 처음 느껴본 문제이다. 앞으로 런타임도 고려해야 겠다. <br/>

- [BOJ 1264](https://www.acmicpc.net/problem/1264) **모음의 개수** <br/>

쉽게 풀었다. 문자열에선 `count` 함수로 특정 문자열이 포함되었는지 확인할 수 있다. <br/>

```python
>> a = 'BlockDMask'
>> print(a.count('k'))
2
```

---

## 20-11-02

- [BOJ 1075](https://www.acmicpc.net/problem/1075) **나누기** <br/>

나는 숫자로 처리했는데, 문자열로 처리하면 더 간단하게 풀 수 있다. <br/>
문자열 처리가 간단해서 파이썬 쓴다는 말을 들은 것 같다. <br/>

- [BOJ 1193](https://www.acmicpc.net/problem/1193) **분수찾기** <br/>

큰 배열에 압도되었지만, 규칙성을 찾으면 아주 쉽게 풀리는 문제다. <br/>

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

- [BOJ 1076](https://www.acmicpc.net/problem/1076) **저항** <br/>

어렵게 풀었다는 생각이 많이 든다... 채점하는 데에 120초나 걸리다니..🤣<br/>
`dictionary`로 데이터를 저장하고 풀었는데, 알고보니 데이터에 규칙이 있어서 `list` 하나로도 간단하게 풀 수 있다. <br/>
아직 `python` 으로 문제푸는 스킬이 부족하단 생각이 많이 든다.<br/>

```python
color = ['black', 'brown', 'red',
'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
f = color.index(input())
s = color.index(input())
t = color.index(input())
r = int(str(f) + str(s)) * (10 ** t)
print(r)
```

- [BOJ 1159](https://www.acmicpc.net/problem/1159) **농구경기** <br/>

문자열 슬라이싱으로 괜찮게 풀었다... 고 생각했지만, <br/>
`counter` 라이브러리를 사용하면 쉽게 풀 수 있단 걸 알았다.😥 그래도 꽤 괜찮게 풀었다. <br/>

```python
from collections import Counter
Counter('hello world')
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
```

- [BOJ 10757](https://www.acmicpc.net/problem/10757) **We love kriii** <br/>

- [BOJ 10718](https://www.acmicpc.net/problem/10718) **큰 수 A+B** <br/>

- [BOJ 10869](https://www.acmicpc.net/problem/10869) **사칙연산** <br/>

- [BOJ 10926](https://www.acmicpc.net/problem/10926) **사칙연산** <br/>

- [BOJ 10998](https://www.acmicpc.net/problem/10998) **AxB** <br/>

---

## 20-11-01

- [BOJ 10172](https://www.acmicpc.net/problem/10172) **개** <br/>

`docstring`이라는 문법이 있다. 나중에 알아보도록 하자.

- [BOJ 10430](https://www.acmicpc.net/problem/10430) **나머지** <br/>

- [BOJ 10699](https://www.acmicpc.net/problem/10699) **오늘날짜** <br/>

`time` 라이브러리를 이용해서 풀었다. 지금은 공부하지 않아도 괜찮을 라이브러리라고 생각해서 넘긴다. <br/>

- [BOJ 1453](https://www.acmicpc.net/problem/1453) **피시방알바** <br/>

C언어로 풀었다. 배열 크기를 101로 잡아줘야 한다. <br/>

---

## 20-10-30

- [BOJ 3003](https://www.acmicpc.net/problem/3003) **킹, 퀸, 룩, 비숍, 나이트, 폰** <br/>

절댓값을 적용해야 한다고 생각했지만, 아니었다.<br/>
`list comprehension`에 리스트를 2개 넣어보려고 `zip` 내장함수를 사용해봤다.<br/>
`zip`은 동일한 개수의 자료형을 묶어주는 역할을 하는 함수이다.<br/>

- [BOJ 3046](https://www.acmicpc.net/problem/3046) **R2** <br/>

- [BOJ 5337](https://www.acmicpc.net/problem/5337) **웰컴** <br/>

여러 줄에 걸쳐 출력할 수 있다는 걸 첨 알았다. <br/>

```python
print(""".  .   .
|  | _ | _. _ ._ _  _
|/\|(/.|(_.(_)[ | )(/.""")
```

- [BOJ 5338](https://www.acmicpc.net/problem/5338) **마이크로소프트 로고** <br/>

- [BOJ 5339](https://www.acmicpc.net/problem/5339) **콜센터** <br/>

- [BOJ 5522](https://www.acmicpc.net/problem/5522) **카드게임** <br/>

리스트를 선언해서 풀었는데, 간단하게 변수 하나에 `input`을 더해주는 방식으로도 풀 수 있다. <br/>

- [BOJ 5554](https://www.acmicpc.net/problem/5554) **심부름 가는 길** <br/>

- [BOJ 6749](https://www.acmicpc.net/problem/6749) **Next in line** <br/>

- [BOJ 7287](https://www.acmicpc.net/problem/7287) **등록** <br/>

- [BOJ 8370](https://www.acmicpc.net/problem/8370) **Plane** <br/>

- [BOJ 8393](https://www.acmicpc.net/problem/8393) **합** <br/>

- [BOJ 8437](https://www.acmicpc.net/problem/8437) **julka** <br/>

- [BOJ 9654](https://www.acmicpc.net/problem/9654) **나무함대 데이터** <br/>

`format`과 함께 출력 형식을 제한한 하는 코드를 써봤다.<br/>

```python
>> print('Python is [{:15}]'.format('good'))
python is [good           ]
```

- [BOJ 10170](https://www.acmicpc.net/problem/10170) **NFC West vs North** <br/>
  출력 형식은 어차피 나중에 구글링하면 되니까.. 그냥 `print`문으로 간단하게 처리했다.<br/>

- [BOJ 10171](https://www.acmicpc.net/problem/10171) **고양이** <br/>

---

## 20-10-29

- [BOJ 1550](https://www.acmicpc.net/problem/1550) **16진수** <br/>

아직도 어떤 문제인지 모르겠다. <br/>
다른 분 코드를 보니 한 줄로 처리되는데, 그걸 보고도 문제 파악이 안된다. <br/>
그래도 `int` 함수의 인자로 진법 변환할 수 있단 걸 알았다. <br/>

```python
# int를 이용한 진법 변환
print(int(input(), 16))
```

- [BOJ 2338](https://www.acmicpc.net/problem/2338) **긴자리계산** <br/>

단순 계산 문제이다. <br/>
새로 배운 건, `print` 함수의 두번째 인자로 `sep='\n'`를 주면, 각 줄에 개행을 넣을 수 있다는 것이다.<br/>

```python
>> print(1, 2, sep='\n')
1
2
```

- [BOJ 2475](https://www.acmicpc.net/problem/2475) **검증수** <br/>

아주 간단한 문제이다. <br/>
`map` 함수로 `input`을 받고, `list comprehension` 문법으로 제곱수 배열을 새로 만들었다.<br/>

- [BOJ 2557](https://www.acmicpc.net/problem/2557) **Hello World** <br/>

- [BOJ 2558](https://www.acmicpc.net/problem/2558) **A+B-2** <br/>

- [BOJ 2845](https://www.acmicpc.net/problem/2845) **파티가끝나고난뒤에** <br/>

간단한 문제이다. `map`과 `list comprehension`에 익숙해지기 위해 사용해서 풀어봤다.<br/>

- [BOJ 2914](https://www.acmicpc.net/problem/2914) **저작권** <br/>

`math` 라이브러리를 `import`해서 `ceil`이라는 올림 함수를 사용해봤다.

---

## 20-10-28

- [BOJ 1000](https://www.acmicpc.net/problem/1000) **덧셈** <br/>

아주 간단한 문제지만, 한 줄에 숫자 여러개 받는 방법을 몰랐다. <br/>
`split()` 함수를 이용하면 `()` 사이에 값을 구분자로 하여 문자열로 나누어 준다. <br/>

```python
# split 함수 예시
>>> a = "Life is too short"
>>> a.split()
['Life', 'is', 'too', 'short']
```

- [BOJ 1001](https://www.acmicpc.net/problem/1001) **뺄셈** <br/>

[BOJ 1000](https://www.acmicpc.net/problem/1000) 와 동일한 문제지만 `int()`로 바로 감싸서 풀었다.

- [BOJ 1271](https://www.acmicpc.net/problem/1271) **엄청난 부자2** <br/>

몫과 나머지의 연산자만 사용하면 아주 간단한 문제였다. <br/>
다른 분의 코드를 보니, `map()`함수를 사용하면 더 간단하게 숫자를 받을 수 있단 걸 알았다. <br/>

```python
# map을 이용한 숫자 입력 예제
n, m = map(int, input().split())
```

---
