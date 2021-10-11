# Kafka

## Kafka 생태계

<img src="../Image/e2edatapipeline.png">

기존 데이터 파이프라인 아키텍처에서는 
- e2e 연결 방식의 아키텍처
- 각각 다른 데이터 파이프라인 연결 구조
- 확장의 어려움

      Linkedin의 데이터팀에서 이러한 문제점을 해결하기 위해 *모든 시스템으로 데이터를 전송*, *실시간 처리가* 가능하고 데이터가 갑자기 많아지더라도 *확장이 용이*한 시스템을 자체 개발한 것이 바로 Kafka

<img src="../Image/afterkafka.png">

- producer/consumer 분리(데이터 제공자, 소비자)
- 메시지 데이터 여러 컨슈머에게 허용
- 높은 처리량을 위한 메시지 최적화
- Scale Out
- 관련 추가 생태계

<img src="../Image/skdataplatform.png">
1. app, was, db의 데이터를 Log definition tool을 통해 정한대로 수집
2. Streaming 데이터는 Kafka, Batch용 데이터는 따로 해서 수집
3. 이를 최종 데이터 저장소인 Hadoop에 저장
4. Hive 등과 같은 EDA툴로 데이터 활용


## Kafka broker, cluster

### Kafka broker
- 실행된 카프카 애플리케이션 서버 중 1대
- 3대 이상의 브로커로 클러스터 구성
- Zookeeper와 연동필요
  - Zookeeper(Apache Zookeeper)
    - Kafka 메타데이터 저장
- 브로커 중 1대는 컨트롤러 기능 수행
  - Controller
    - 각 프로커에게 담당파티션 할당
    - 브로커 정상 동작 모니터링