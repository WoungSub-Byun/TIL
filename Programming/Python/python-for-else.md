# Python 문법 - for ~ else

일반적인 프로그래밍언어들에서  ```else```는 if와 같이 사용되며 조건에 일치하지 않는 경우에 실행되는 구문을 표시하는 문법입니다.

하지만, Python에서는 ``` if ``` 뿐만이 아니라  ``` for ```문에서도 사용됩니다.

> 사용방법
> - *```for```와 함께 쓰이는 ```else```는 ```for```문이 중간에 break 등으로 끊기지 않고 끝까지 수행 됬을 때 수행하는 코드를 담고 있습니다.*

> 사용이유
> - 코딩을 하다 보면 **flag변수**를 사용하여 Yes/No의 상태를 나타내어 조건에 부합하거나 부합하지 않는 경우에 실행할 구문을 구분하곤 합니다.
> Python에서는 ```for~else```문을 사용하여 간단하게 flag와 같은 기능을 구현할 수 있습니다.

> 사용예시
```python
def example():
    data = [1,2,2,,4,5,7,9]
    answer = True
    for i in data:
        if i > 10:
            answer = False
            break
    if answer:
        print('10보다 큰 원소 없음')
```
- 위의 코드는 for 반복문을 사용해 리스트 안에있는 원소들중 10 이상의 값이 있는지 판별해 해당하는 구문을 실행하는 코드입니다. 이를 ```for~else```문을 사용하여 구현할 수 있습니다.
```python 
def example():
    data = [1,2,2,,4,5,7,9]
    for i in data:
        if i > 10:
            break
    else:
        print('10보다 큰 원소 없음')
```
- 위와 같이 ```answer```라는 flag 변수를 사용하지 않고도 간편하게 구현할 수 있습니다.


> +python에는 try~else문도 존재한다.