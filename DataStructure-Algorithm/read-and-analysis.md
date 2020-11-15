# 읽기와 분석 (시간복잡도/공간복잡도)
---

### 📄 읽기와 분석
- 알고리즘 문제 해결의 가장 중요한 것
- 문제의 조건들을 추상화하는 연습
- 시간복잡도/공간복잡도 어림잡기

### 시간복잡도
---
- 어떤 이유로 코드의 실행 시간이 오래 걸릴까? => **연산량**
- 연산량은 어떤 값과 상관이 있을까? => **입력**

- 모든 연산을 Counting 할 수 있을까? => **X**
- 최악의 경우와 최선의 경우? => **X**
- Counting에 따라 실행시간은? => **X**
=> 다양한 이유(하드웨어 차이, 연산 처리속도 등등)로 **정확한 실행시간이나 시간복잡도를 구하기는 힘들다**

그래서!

#### 😁 **대충 계산하자 => 점근적 표기법**
표현법 : **Big-O Notation**
- 입력이 N일때, 연산 횟수가 최악이 2N^2 + 4N이라면? 
- **O(N^2)**
*N이 무한대로 커질 때, 가장 많은 영향을 주는 항은 최고차항이다!*
![big-onotation](https://miro.medium.com/max/550/1*k-acuFitTKegB5l5JTn0tA.png)




### 문제풀이 할 때는 최악의 경우를 생각하자!

## 문제 푸는 순서
1. 시간, 메모리, 입력, 출력 보고 풀이 감 잡기
  - ### 표현법과 감
  - 시간과 공간 차원에서 각각 다를 수 있음 => 시간 복잡도와 공간복잡도
  - 계선 + 시스템에 대한 감(센스)이 중요
  ![pythonspeedimage](../Image/pythonspeedimage.png)
2.  Naive(무작정)한 풀이 떠올리기
3. 중간 과정에 반드시 필요한 로직 생각하기
4. 예제 입력과 예제 출력 매칭
5. 코드 작성

## 입력과 초기화 팁 - Map과 Comprehension
---
입력의 대표적인 사례 3가지
- 수
- 문자열(문자 배열)
- 배열

- Map(x, y)
  - x함수를 y의 원소에 모두 적용한 map 객체를 반환
```python
# 문자로 입력된 4개의 숫자를 int형으로 만들어 출력
num = [input() for i in range(4)]
print(map(int, num))
```
- List Comprehension
  - List 초기화는 comprehension으로!
```
n_list = [0 for _ in range(n)]
```

## 에러 메시지 - Accepted와 Wrong Answer
---
![errormsgimage](../Image/errormessageimage.png) 