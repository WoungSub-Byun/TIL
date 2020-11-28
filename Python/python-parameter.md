# python parameter - args, kwargs
---
Python 함수 선언부에 보면 가끔 args, kwargs를 볼수 있다.

- args : 정해지지 않은 수의 (일반)파라미터를 받는다
- kwargs : 정해지지 않은 수의 (키워드)파라미터를 받는다
  ? 이게 무슨 소릴까 차근차근 이해해보자

### Python의 Parameter
- 일반 파라미터
```python
def myFunc(a, b):
    return a + b
myFunc(1, 2)
```
위와 같이 일반적으로 사용하는 파라미터
- 키워드 파라미터
```python
def myFunc(a=0, b=1):
    return a + b
myFunc(1, 2)
```
위와 같이 파라미터의 이름과 함께 default값을 지정한 파라미터
일반적으로 파라미터를 받는 방식으로 받으면 되지만, 
```python
def myFunc(a=0, b=3, c=1):
    return a + b + c
```
위의 경우에서 a,b는 기본 인자 값 그대로 사용하고 c에만 다른 값을 넣어주고 싶을 경우
```python 
myFunc(c=4)
```
이렇게 호출하는 쪽에서 변수명(키워드)를 지정해주면 된다.

하지만 키워드 인자는 일반 인자 뒤에 와야 한다. 또한 호출할 때에도 일반 인자 뒤에 와야한다.
```python
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    ...
# 가능
parrot(1000)
parrot(voltage=1000)
parrot(voltage=1000000, action='VOOOOOM')

# 불가능
parrot()                     # 일반 인자값 없음
parrot(voltage=5.0, 'dead')  #키워드 인자 뒤에 일반 인자값을 주지 못함
parrot(110, voltage=220)     # 한 인자에 두 값을 주지 못함
parrot(actor='John Cleese')  # actor라는 키워드가 없음
```

이제 args와 kwargs를 보자

**kwargs는 딕셔너리 형태로 키워드 인자들 중에서 일반 인자가 아닌 것들을 넘겨 받는다.
*args는 일반 인자값을 받으므로 **kwargs와 혼용하는 경우 반드시 **kwargs가 뒤에 와야 한다.
```python
def myFunc(a, *args, **kwargs):
    print('a=', a)
    print('args=', args)
    print('kwargs=', kwargs)

>>> myFunc(11)
a= 11
args= ()
kwargs= {}
>>> myFunc(11,22,33) #일반 인자 값이기 때문에 22, 33은 args에 들어간다
a= 11
args= (22, 33) #type : <class 'tuple'>
kwargs= {}
>>> myFunc(11,22,33,b=44,c=55) # 키워드 인자 b, c는 kwargs에 들어간다.
a= 11
args= (22, 33)
kwargs= {'c': 55, 'b': 44} # type : <class 'dict'>
```