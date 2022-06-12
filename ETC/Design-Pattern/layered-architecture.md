# 레이어드 아키텍처 - Layered Architecture
---

## Architecture Pattern- 아키텍처 패턴이란?

- Wikipedia
> 주어진 상황에서의 소프트웨어 아키텍쳐에서 일반적으로 발생하는 문제점들에 대한 일반화되고 재사용 가능한 솔루션이다. 아키텍쳐 패턴은 소프트웨어 디자인 패턴과 유사하지만 더큰 범주에 속한다.

즉, 소프트웨어의 전체적인 구조를 잡아줍니다.
어떤 상황에 어떤 아키텍처를 사용하는지에따라 성능에 차이가 날 수 있기때문에 적절한 아키텍처를 선택해야합니다.

## Layered Arichitecture ?

- == n-tier Architecture Pattern
- 계층화 아키텍처 패턴

레이어드 아키텍처는 하위 모듈들의 그룹으로 나눌 수 있는 **구조화된 프로그램**에서 사용할 수 있습니다. 각 모듈은 특정한 수준의 **추상화**를 제공합니다. 이 떄 상위 계층의 추상화 수준은 일반적으로 다음과 같습니다.

> - **Presentation Layer**
> - **Application Layer**
> - **Business logic Layer**
> - **Data Access Layer**

![archiimg](https://dzone.com/storage/temp/4277164-layered-architecture-overview.png)

1. Presentation Layer
   - UI 계층으로도 불림
   - 직역하면 '표현 계층'이라고 불리는데, 클라이언트에게 표현해주는 단계라고 볼 수 있습니다.
   - ***request*** 를 직접 받는다.
  
2. Application Layer
   - 서비스 계층으로도 불림
   - 상호작용하는 서비스에 필요한 정보를 전달하는 레이어라고 볼 수 있습니다.
3. Business Layer
    - 도메인 계층으로도 불림
    - 실제 시스템의 로직이 구현되어있는 레이어라고 볼 수 있습니다.
4. Data Access Layer
    - 영속 계층이라고도 불림
    - 데이터베이스 관련 로직들을 처리하는 레이어입니다.

## 사용
일반적인 e-commerce나 웹 어플리케이션에서 자주 사용합니다.

## Controller, Service, Model

1. Controller
- Presentation Layer에 해당합니다.
- 직접 엔드포인트를 정의하고 request를 받는 모듈입니다.
- 중복을 처리하기위해 별도의 객체로 분리하고 이를 메소드로 분리합니다.

2. Service
- Business Logic을 수행하는 메소드를 가지고 있는 부분입니다.
- 하나의 비즈니스 로직은 하나의 트랜잭션으로 동작하는 것이 일반적입니다.

* **트랜잭션**
> - 원자성 (Atomicity)
>   - rollback - 변경사항 취소
>   - commit - 변경사항 저장
> - 일관성 (Consistency)
>   - 트랜잭션이 진행되는 동안에 데이터가 변경되더라도 업데이트된 데이터로 트랜잭션이 진행되는 것이 아니라, 처음에 트랜잭션을 진행하기 위해 참조한 데이터로 진행된다.
> - 독립성 (Isolation)
>   -  하나의 특정 트랜잭션이 완료될 때까지, 다른 트랜잭션이 특정 트랜잭션의 결과를 참조할 수 없습니다.
> - 지속성 (Durability)
>   - 트랜잭션이 성공적으로 완료됬을 경우, 결과는 영구적으로 반영되어야 한다.

3. Model
   - ORM이 사용된다면 일반적으로 데이터베이스와 테이블을 정의하고 Service에서 객체를 생성하여 로직을 처리합니다.

## 레이어드 아키텍처의 장점
- 확장성 용이
- 유지 보수 용이
- 코드 가독성 🔼
- 재사용성 🔼
- 테스트 구현 용아