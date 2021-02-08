# Pycon Apac 2016 - Django vs Flask
Speaker : 김도현(선린인터넷고등학교)

## django, flask 왜 쓸까?
> ***불편하니까!***

웹 통신을 구현한다고 하면
1. HTTP 프로토콜을 일일히 파싱한 다음
2. HTTP methods에 따라 동작을 나누고
3. HTML 렌더링 엔진을 만든후 포맷스트링에 맞추어 원하는 변수를 html에 표시하고
4. 웹 서버를 거쳐 배포

* DB작업까지 한다면...?

이런 똑같은 작업의 반복을 피하고 복잡한 문제를 줄이며 주어진 시간내에 작업을 끝마치기 위해 구현하기 벅찬 기능들을 사용하려고 사용하는 것

## django vs flask 
### intro
|  | initial release | Slogan | User |
|---|---|---|---|---|
|django|21 July 2005|*The web framework for perfectionists with deadlines*|DeliveryHero, Pinterest, instagram|
|Flask|April 1 2010|*Web development, One drop at a time*|StyleShare, 로켓펀치, 번개장터|

### comparison
- Django ORM vs SQLAlchemy
- Form vs flask-wtf
- Template Engine vs Jinja2
- Admin Page vs flask-admin
- south(migrate, makemigrations) vs alembic
- Middleware vs before_request, after_request 혹은 wsgi 단에서 직접 구현
- manage.py vs flask-scripts
- manage.py test vs unittest or flask-test
- def view(request) vs flask.request
- django.contrib.messages vs flask.flash

### Difference
- Django : Meta 프로그래밍의 결정체
    - 추상화도 많고 상속하는 관계가 매우 많음
- SQLAlchemy -> ManyToMany 지원하지 않음
- get_object_or_404, get_or_create =>
- REST API 구현할때
    - 흔한 작업 할때는 django
    - 변동이 많을 때는 Flask => Custom 할 수 있게

> *Django 암시적이지만 많은 것들  vs  Flask 명시적이지만 부족한 것들*

### 내생각
- Flask가 더 마음에든다. 웹 개발에 대한 전반적인 지식이 없는 상태에서 빨리 기능을 구현해야한다면 django가 낫겠지만 기본을 이해하는데는 Flask가 더 낫다고 생각한다. 하나하나 구현해가면서 이해하는 것이 좀 더 마음에 든다.