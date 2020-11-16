# 알고리즘과 수학
---
- 진수, 진법
- 최소공배수, 최대공약수
- 
## 진수와 진법
---
- N 진법으로 문자열을 변환하기
```python
def stoi(s, n):
    ret = 0
    l = len(s)
    for i in range(l): ret += int(s[i]) * n**(l-i-1)
    return ret
```
=> 활용
- 거듭제곱 연산
[baekjoon1629번](https://www.acmicpc.net/problem/1629)
- 조건문 + N진수 변환 방법으로 해결 가능
![doublemulimage](../../Image/doublemulimage.png)
```python
def pow_custom(a, b):
    ret = 1
    while b:
        if b % 2 == 1: ret *= a
        a = a*a
        b //= 2
    return ret
```
- 큰 수를 곱하는 것은 Python에서도 느리기 때문에 모듈러 연산자를 중간중간에 쓰자!
  

## 최대공약수와 최소공배수
---
- **최대공약수(GCD)** : 공약수 중 최댓값
  - 최대공약수가 1이면 **서로소**
- **최소공배수(LCM)** : 공배수 중 최소값

> **LCM(A, B) = A * B / GCD(A, B)**

=> **GCD만 잘 구하면 LCM은 O(1)에 구할 수 있다.**

- 최대공약수 
```python
# 정방향 체크
def gcd(a, b):
    ret = 0
    for i in range(min(a, b)):
        if a % i == 0 and b % i == 0:
            ret = i
    return ret

# 역방향 체크 => 더 빠름
def gcd(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i
```
- ✅ 😀**유클리드 호제법** 
  - 위의 두 방식보다 훨씬 빠르다
> **GCD(A, B) = GCD(B, A % B)**
```python
# 속도 => O(log N)
def gcd(a, b):
    return b if a % b == 0 else gcd(b, a%b)
```