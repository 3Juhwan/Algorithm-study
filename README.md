# 알고리즘 스터디

<br />

> 공부하려고 만들었습니다.  
> 빨리 취업하고 싶습니다.

<br/>

백준 닉네임 : **`3Juhwan`**<br/>

### 메모

**20-10-28** <br/>
공부 시작! 🔥🔥<br/>
하루에 3문제 이상 풀면서 감 잡기!!<br/>

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
