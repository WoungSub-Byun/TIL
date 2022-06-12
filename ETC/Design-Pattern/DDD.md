# 도메인 주도 설계 (DDD)

### 문제점

- 소프트웨어 개발과 도메인, 모델과의 불일치 발생(도메인이 복잡하기 때문)
- 기획과 개발의 불일치 발생
- 소통 어려움

        도메인 - 추상화 -> 모델 - 실체화 -> 소프트웨어

### 해결방안

- 보편언어 선택
- 모델 주도 설계

### 종류

- 전략적 설계
  - 비즈니스의 상황에 맞게 설계
  - 모든 Context를 이벤트 스토밍을 통해 공유
  - 각 Context를 그룹핑(Bounded Context)
  - Context Mapping을 통해 Bounded context 간의 관계를 정의

-> 전략적 설계의 결과물: 도메인 모델(서비스를 추상화한 설계도, 분리 & 연결)

- 전술적 설계
  - 더 상세한 부분 (Bounded Context 내부) 모델링
  - Model driven design
  - Aggregate pattern

=> DDD는 개발하는, 기술적인 방법이 아닌 기획자와 개발자간의 간극을 줄여주기위한 방법론에 해당

## 이벤트 스토밍

- 이벤트는 Actor가 Action을 해서 발생한 결과
- 비즈니스 용어로 무슨 일이 발생했는지를 적는 것 -> 시스템 내에서 발생되는 것을 찾는게 아님

- 단계
  - Domain Event 정의
  - 프로세스 그룹핑
  - Command 정의
  - Trigger 정의
  - Aggregate 정의
  - Bounded Context 정의
  - Contexts Map 작성
