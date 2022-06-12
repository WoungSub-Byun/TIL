# ORM - Object Relational Mapping)
---

## 개념
- 객체와 **관계형 데이터베이스**의 데이터를 자동으로 **매핑(연결)**해주는 것입니다.
  - 객체 지향 프로그래밍에서의 **클래스** == RDB의 **테이블**
  - 객체 모델과 관계형 모델 간의 불일치(객체 임피던스 부조화) 문제가 존재합니다.
  - ORM을 사용해 객체 간의 관계를 바탕으로 **SQL을 자동 생성**하여 불일치 문제를 개선합니다.

## 장/단점
> **장점**
- 객체 지향적인 코드로 인해 더 직관적으로 로직에 집중할 수 있습니다.
  - ORM을 사용하여 데이터베이스와의 **CRUD 작업을 SQL(Raw) Query가 아닌 코드(메서드)로 사용**할 수 있습니다.
  - 객체에 대한 코드를 별도로 작성하기 때문에 **코드의 가독성**이 올라갑니다.
- **재사용 및 유지보수의 편리성**
  - ORM은 독립적으로 작성되어 있고, 해당 객체들을 **재사용**할 수 있기 때문에 모델에서 가공된데이터를 컨트롤러에 의해 뷰와 합쳐지는 형태로 **디자인 패턴(MVC, MVT 등등)을 견고하게 다지는 데 유리**합니다.
- **DBMS에 대한 종속성 감소**
  - 대부분의 ORM 솔루션은 DB에 종속적이지 않고, 객체 간의 관계에 따라 SQL을 자동으로 생성하기 때문에 각기 다른 DBMS에 맞추어 설계할 필요가 없습니다.
  - 객체에 집중함으로써 DBMS를 교체하는 거대한 작업에서 비교적 적은 리스크와 시간이 소요됩니다.
> **단점**
- **ORM으로만 서비스를 구현하기는 어렵습니다.**
  - 사용하기 편하지만 프로젝트의 복잡성이 커질경우 난이도 또한 올라가기 떄문에 **설계를 매우 신중**하게 해야합니다.
  - 자동으로 SQL을 생성해주기 때문에 생성되는 쿼리에 **불필요한 제약들**이 올라가기도 하며 **쿼리의 속도가 하락**합니다.

## 사용
 - Python
   - SQLAlchemy
   - Django Framework => ORM을 기본 제공
 - Java
   - Hibernate
   - JPQL
   - Mybatis & JPA
 - Javascript
   - Sequelize.js
   - TypeORM  등등
  
## 객체-임피던스 부조화 (The Object-Relational Impedance Mismatch)
![object-relationalimage](https://gmlwjd9405.github.io/images/database/orm-impedance-mismatch.png)
- **세분성**
  - 경우에 따라 **DB에 있는 테이블 수보다 더 많은 클래스를 가진 객체 모델**을 가질 수 있습니다.
    - 예를 들어, 사용자 세부 사항이라는 테이블을 생각해봅시다.
    - Person과 Address라는 두개의 클래스로 나누어 질 수 있지만 DB에는 person이라는 하나의 테이블에 사용자 세부 사항을 저장할 수 있습니다.
    - Object : 2개 != Table : 1개
- **상속**
- **일치**
  - **RDB에서는 기본키**(PK)를 사용하여 'sameness'의 개념을 정의하지만 **프로그래밍 환경에서는 주소값이 같거나 내용이 같은 경우를 구분**하여 정의 합니다.
- **연관성**
- **탐색**