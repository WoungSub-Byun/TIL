# Kafka

- LinkedIn 데이터팀에서 개발한 분산 데이터 스트림 처리 도구
  <img src="https://uploads-ssl.webflow.com/5f3b26c29dba8735d06ae72c/6018c104cc4d9ac1f4137dd1_20210202-apache_kafka-ar21.png">

## Kafka는 왜 만들어졌는가?

기존의 데이터 파이프라인 아키텍처
<img src="https://mblogthumb-phinf.pstatic.net/MjAxODA3MTdfODMg/MDAxNTMxODA4NzUwNTg5.sONkmFq9AOH9Ve1bsEmsjwMurzeGE_nN4L3qPUQJCDMg.Q9bPGBzg6n5jb_8_Dv264lnxbdwL4sFXQaAJnrw9sTIg.PNG.clwmrjf/LinkedIn_Logo.png?type=w800">

- 기존의 아키텍처에서는 redis나 rabbitMQ와 같은 서비스들을 사용하고 있었는데 이는 *각 애플리케이션마다의 특징을 모두 맞추어야하는 문제점*을 만들어냈다.
- 즉, **데이터 파편화가 심각**해졌고 이는 **서비스의 유지보수를 어렵게 만들었다.**

위 문제점을 해결하기 위해

- 데이터의 중앙집결화
- 대용량 데이터 실시간 수집
- 사용자의 실시간 스트림으로 데이터 소비

할 수 있는 도구가 필요했고 그 도구가 바로 **Kafka** 이다.

## Kafka의 특징

1. High throughout messaging capacity

- 짧은 시간안에 데이터의 처리 가능

2. Scalability와 fault tolerent : 확장성과 고가용성

- broker와 replication을 활용하여 쉽게 확장할 수 있고 브로커가 죽더라도 복제된 다른 브로커에서 쉽게 복구가 가능하다.

3. Undeleted Log

- 타 플랫폼과 달리 컨슈머가 데이터를 소비해도 데이터는 삭제되지 않는다.

## Kafka의 사용성

여러 애플리케이션에서 나오는 빅 데이터 수집 및 처리 시스템

- 하지만 소규모의 스타트업에서도 사용하는 것을 추천한다.
  그 이유는 바로 **확장성과** **고가용성**에 있다.
  스타트업은 급속도로 성장할 수 있기 때문에 높은 확장성을 필요로 한다. Kafka는 broker를 통해 쉽게 확장시킬 수 있고 만약 브로커에 문제가 생기더라도 replication을 통해서 쉽게 복구가 가능하기 때문에 쉽게 도입할 수 있다.
