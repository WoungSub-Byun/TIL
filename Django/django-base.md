# Django
---
- Django framework를 사용하여 개발하면서 공부한 잡다한 개념들을 적은 곳

#### django 프로젝트 기본적인 생성 및 설정

```bash
# 가상환경 생성하기
$ python3 -m venv [가상환경 이름] #python 내장 가상환경 만들기
# in UNIX
$ source [가상환경이름]/bin/activate
# in CMD
$ [가상환경이름]\Scripts\activate

# django 설치
(venv) $ pip install django black # black: python 자동 포맷팅 라이브러리

# django 프로젝트 생성
(venv) $ django-admin startproject [프로젝트 이름]
(venv) $ cd [프로젝트 이름]

# django 앱 생성
(venv) $ python manage.py startapp [앱 이름]

# django 프로젝트 실행
(venv) $ python manage.py runserver
# 포트를 바꾸어 실행하고 싶을 때
(venv) $ python manage.py runserver [바꿀 포트]
# localhost가 아닌 다른 IP로 실행하고 싶은 경우
(venv) $ python manage.py runserver [IP]:[바꿀 포트]

# admin 페이지 사용을 위해 superuser 생성
(venv) $ python manage.py createsuperuser
... 나오는 정보들 입력...
Superuser created successfully.

```
- 가장 바깥의 root directroy는 프로젝트의 컨테이너일 뿐이라 이름을 바꿔도 상관없다.
- ```manage.py``` : django 프로젝트와 상호작용할 command-line utility
- 안쪽의 프로젝트이름으로 만들어진 default app 디렉토리가 실질적인 프로젝트의 패키지이다.
- ```runserver```를 실행하게 되면 django에서는 기본적으로 ```localhost:8000```으로 실행된다. 



#### django model queryset
---
django는 ORM을 제공한다. ORM을 효과적으로 사용한다는 것은 ORM이 쿼리를 어떻게 작성하는지 이해하는 것이다.

- **django의 쿼리는 마지막까지 지연된다.**
django의 queryset은 DB의 여러 레코드를 나타내고 필터링이 가능하다
```python
person_set = Person.objects.filter(name="Tom")
```
**이 코드는 DB에 어떤 쿼리도 전달하지 않는다.**
이는 DB에 아무런 메시지도 전달하지 않는다는 점에서 장점이다. 왜냐하면 DB에 쿼리를 전달하는 일이 웹 애플리케이션을 느려지게 하는 주범 중 하나이기 때문이다. 
- **django의 쿼리셋은 캐시된다.**
django queryset을 순회하는 시점에서 DB의 레코드를 실제로 가져오고, 이는 모두 **django 모델로 변환되어 캐시된다**(**평가**). 따라서 queryset을 다시 순회하더라도 똑같은 쿼리를 DB에 여러번 전달하지 않는다.

- **if문은 쿼리셋을 평가한다.**
캐시 기능은 queryset에 레코드가 존재하는지를 검사한 후 하나라도 발견되었을 때만 순회하려 할 때 유용하다.
```python
person_set = Person.objects.filter(gender='male')
# if 문은 queryset을 '평가'한다.
if person_set:
    for person in persion_set:
        print(person.name)
```
하지만, 결과 전체가 필요하지 않고 단지 레코드가 최소한 하나는 존재하는지 알아보고 싶을 경우에는 if 문을 사용하면 queryset이 평가되고 queryset 캐시에 전체 레코드가 저장되는 비효율적인 작업이 일어나게된다.
이럴떄는 exists() 메서드를 사용하자
```python
person_set = Person.objects.filter(name='Tom')
# if 문은 queryset을 '평가'한다.
if person_set.exists():
    # DB에서 가져온 레코드가 하나도 없다면 트래픽과 메모리를 절약할 수 있다.
    print('Tom exists')
```


## django-rest-framework
---
- django를 사용해 web API를 개발 할때 자주 사용되는 serializer, permisison, authentication, view 등의 기능을 편리하게 사용할 수 있게 만든 라이브러리
  
- Installation
```
$ pip install djangorestframework
```
- in INSTALLED_APPS
```
'rest_framework' 추가
```

> serializer.save() 하기전 serializer.is_valid()를 해야한다.
- ```rest_framework\serializers.py```
```python
def save(self, **kwargs):
        assert hasattr(self, '_errors'), (
            'You must call `.is_valid()` before calling `.save()`.'
        )

        assert not self.errors, (
            'You cannot call `.save()` on a serializer with invalid data.'
        )

        # Guard against incorrect use of `serializer.save(commit=False)`
        assert 'commit' not in kwargs, (
            "'commit' is not a valid keyword argument to the 'save()' method. "
            "If you need to access data before committing to the database then "
            "inspect 'serializer.validated_data' instead. "
            "You can also pass additional keyword arguments to 'save()' if you "
            "need to set extra attributes on the saved model instance. "
            "For example: 'serializer.save(owner=request.user)'.'"
        )

        assert not hasattr(self, '_data'), (
            "You cannot call `.save()` after accessing `serializer.data`."
            "If you need to access data before committing to the database then "
            "inspect 'serializer.validated_data' instead. "
        )

        validated_data = {**self.validated_data, **kwargs}

        if self.instance is not None:
            self.instance = self.update(self.instance, validated_data)
            assert self.instance is not None, (
                '`update()` did not return an object instance.'
            )
        else:
            self.instance = self.create(validated_data)
            assert self.instance is not None, (
                '`create()` did not return an object instance.'
            )

        return self.instance
```
