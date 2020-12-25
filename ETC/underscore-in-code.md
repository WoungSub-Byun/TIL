# underscore(_) in coding
---
코딩을 하면서 수많은 변수명을 짓는다.
변수명은 아무렇게나 짓는것이 아닌 특정한 의미를 가지는 그중에서도 언더스코어를 사용할 때의 의미를 알아보자

## in General
- 보통 띄어쓰기의 의미로 쓴다.
> 프로그래밍 언어에서 dash(-)는 'minus'의 의미로 많이 사용되기 때문에 띄어쓰기는 보통 언더스코어로 많이 표현한다.

## in Python
- python에서는 ```for ~ in ~```의 형태로 for반복문을 사용한다. 
- ```for in``` 구문의 장점은 어떠한 데이터의 원소들을 하나씩 꺼내서 사용할 수 있다는 것이다.
- 하지만 아래의 코드처럼 개체를 사용하는게 아닌 단순한 반복 작업 수행의 목적이라면 장점이 사라지게 된다.
```python
for i in range(10):
    print('Hello World')
``` 
- 이때 underscore(_)를 사용하면 변수의 갑을 무시함을 표현한다.
```python
for _ in range(5):
    print('Hello World')
```
