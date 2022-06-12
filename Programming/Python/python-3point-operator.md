# 3항 연산자 in Python
---

### 3항 연산자란?
- 대부분의 프로그래밍 언어에서 제공하는 연산자들에는 산술연산자(+,-,*,/,%,**,//), 비교 연산자(==, !=, >, <, >=, <=), 논리연산자(and, or, not) 등 다양한 연산자들이 있습니다.
- 이 중에서도 용이하게 쓰이는 연산자가 있는데 바로 3항 연산자입니다.
- 일반적으로는 ```condition ? when True : when False``` 의 형태를 지니는데 Python에서는 사용방법이 조금 다릅니다.

### Python의 3항 연산자 사용법
---
- Python에서 3항연산자를 사용하는 방법은 2가지가 있습니다.



#### ```and```와 ```or```을 이용한 연산
  ```python
    condition and when True or when False
  ```
- 3항연산자의 condition이 True이면 and 뒤의 연산이 실행되고, False라면 or 뒤의 연산이 실행됩니다.
    - 풀이
        - Python에서 ``` a and b or c```라는 연산이 있습니다. 해당 연산을 실행하게 되면 이 연산은 ``` (a and b) or c```로 바뀌어 ``` a and b```를 먼저 확인합니다. a가 True이면 b를 확인하고 a가 False이면 c를 바로 확인합니다. 만약 a와 b가 모두 True이면 c를 확인할 필요가 없기 때문에 바로 b를 return 해줍니다. 반대로 a가 False이면 c의 값이 어떤 값이던 c의 값이 결과가 되기 때문에 c를 return 해줍니다.
    ###### 문제점
    > **하지만**, 위의 연산방식에는 결함이 존재했습니다.
    ```python
    a = 1
    b = 1
    result = a == b and a-b or a+b
    ```
    해당 연산을 실행해보면 20이라는 결과가 나오게 됩니다. a-b 즉, 0이 return되어야 하는데 무언가 이상하죠?
    해당 문제는 and 뒤가 0일 경우에 발생합니다. 컴퓨터에서 0은 곧 False를 의미하기 때문에 a == b and a-b는 False가 나오게 되고 a+b는 2, 즉 True이기 때문에 a+b를 반환하게 됩니다.
    이 문제를 보완하기 위해 Python 버전 2.5부터 다른 방식이 나타나게 됩니다.

#### if와 else를 이용한 연산
- 표현
```python
a = 1
b = 1
result = a - b if a == b else a + b
```
- if 뒤의 조건이 True일 경우 if 앞의 연산을 실행하고 False라면 else 뒤의 연산을 실행합니다. 생소한 표현이지만 Python에서는 유용하게 쓰입니다.
- ```for```를 사용해 List에 원소를 집어넣을때
```python
list = [ idx for idx in items ]
```
