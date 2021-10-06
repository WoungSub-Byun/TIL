# Monolithic vs Microservice

<img src="../Image/monolithic-vs-microservices.png">

## Monolithic

- 하나의 애플리케이션에 모든 기능들을 구성하는것

- 장점
  - e2e 테스트 용이
  - 빠르게 서비스 개발 가능
- 단점
  - 유지보수 힘듬
  - 일부분의 수정이나 오류가 전체에 영향을 미침

## Microservice

- 기능을 여러개의 애플리케이션으로 분배시켜 통합하여 구성

- 장점
  - 유지보수 용이
  - 거대한 서비스도 빠르게 수정 가능
- 단점
  - 모니터링이 힘듬
  - e2e 서비스 구동에 불편
  - monolithic에 비해 초기 개발 속도 느림
