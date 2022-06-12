# Thread(스레드)

최근 회사 실무 면접을 보면서 CS질문을 받았는데 제대로 답변하지 못했던 스레드에 대해서 공부했다.

## 프로세스(process) vs 스레드(thread)

### 프로세스

사용자가 작성한 프로그램이 운영체제에 의해 **메모리 공간을 할당받아 실행 중**인 상태

- 구성
  - 프로그램에 사용되는 데이터나 메모리
  - **스레드**

### 스레드

**프로세스 내에서 실제로 작업을 수행하는 주체**

- 모든 프로세스에는 한 개이상의 스레드가 돌아가며 작업을 수행함
- 멀티 스레드 프로세스: 두 개 이상의 스레드를 가지는 프로세스

## 멀티 스레드

하나의 프로세스 내에서 **둘 이상의 스레드가 동시에 작업을 수행**하는 것

- 멀티 프로세스: **여러개의 CPU를 사용하여 여러 프로세스를 동시에 수행**하는 것

### 멀티 프로세스 vs 멀티 스레드

- 멀티 프로세스
  - 각 프로세스가 독립적인 메모리를 가지고 별도로 실행
- 멀티 스레드
  - 각 스레드가 자신이 속한 프로세스의 메모리를 공유
- 특징
  - 시스템 자원의 낭비 적음
    - 각 스레드가 자신이 속한 프로세스에 할당받은 메모리를 공유하여 사용하기 때문
  - 사용자와의 응답성 좋아짐
    - 하나의 스레드가 작업을 할 때 다른 스레드가 별도의 작업을 할 수 있기 떄문

## Context Switching

컴퓨터에서 동시에 처리할 수 있는 작업수는 **CPU의 코어(core)수** 인데, 만약 이 코어 수보다 많은 스레드가 실행되면 *각 코어가 정해진 시간 동안 여러 작업을 번갈아가며 수행*하게 된다.
이 때 *각 스레드가 서로 교체되는 상황에서 Context Switching이 발생*한다.

Context Switching이란 **현재까지의 작업 상태나 다음 작업에 필요한 각종 데이터를 저장하고 읽어오는 작업**을 말한다.

*멀티 스레드 환경에서 Context Switching에 걸리는 시간이 커질수록 효율은 저하*되고 *많은 양의 단순한 계산은 싱글 스레드로 동작하는 것이 효율적*이다.

## 스레드 그룹(thread group)

서로 관련이 있는 스레드를 하나의 그룹으로 묶어 다루기 위한 장치

## 데몬 스레드(daemon thread)

다른 일반 스레드의 작업을 돕는 *보조적인 역할*을 하는 스레드

일정 시간마다 자동으로 수행되는 저장 및 화면 갱신 등에 이용

대부분 무한 루프와 조건문을 이용하여 실행 후 대기하고 있다가 특정 조건이 만족되면 작업을 수행하고 다시 대기하도록 작성

## 가비지 컬렉터(garbage collector)

프로그래머가 동적으로 할당한 메모리 중 _더 이상 사용하지 않는 영역을 자동으로 찾아내어 해제해 주는 데몬 스레드_

가비지 컬렉터가 동작하는 동안에는 프로세서가 일시적으로 중지되기 때문에 성능의 저하가 발생하지만 최근에는 가비지 컬렉터의 성능이 많이 향상되어 새로 만들어지는 대부분의 프로그래밍 언어에서 가비지 컬렉터를 제공하고 있다.