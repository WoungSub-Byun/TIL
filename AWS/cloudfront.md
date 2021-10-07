# AWS Cloudfront

<img src="../Image/cloudfront.png">

- Cloudfront = Cache + CDN
- 기본적으로는 Cache 서버
- Cache 서버는 전 세계에 있는 인프라 활용
  -> Edge location 사용

### 필요성

기존의 웹 호출 방식

- 클라이언트가 요청할 때마다 서버가 응답해주는 방식
- 각 요청마다 HTML 문서를 동적으로 생성
- 느린 UX 속도
- 불필요한 서버비용 발생

### 해결방안

- 클라이언트가 요청하여 응답된 결과를 cahce로 저장 -> in cache server
- 첫번째 요청 이후부터는 기존 server에 요청할 필요 없이 cache server에 요청하여 저장된 정보 추출
- 요청마다 동적 생성 X, 정적 데이터로 응답

## CDN

<img src="../Image/cdn.jpeg">

- Content Delivery Network
- 전세계 어느 위치에서 접속하더라도 빠른 속도로 서비스할 수 있도록 하는 서비스
- Edge Location(Cache Server)활용
