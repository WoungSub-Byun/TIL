# REST- RESTFul - REST API

![restimg](https://media.vlpt.us/images/dnjscksdn98/post/c0ee49ed-ced7-4b50-be62-ab645a031b98/rest_logo.png)
## REST
* Full name
> "Representational State Transfer"
- 직역하면 '대표 상태 전송'

## REST의 구성
- 자원(resource) - URI
- 행위(Verb) - HTTP METHOD
- 표현(Representations)

## REST의 특징

### 1. Uniform
- Uniform Interface
  - URI로 지정한 자원에 대한 조작을 통일되고 한정적인 인터페이스로 수행하는 아키텍처 스타일

### 2. Stateless - 무상태성
- 작업을 위한 상태를 따로 저장하지 않는다.
- 세션 정보나 쿠키정보를 따로 저장하고 관리하지 않기때문에 API 서버는 들어오는 요청만을 단순히 처리한다.

### 3. Cacheable - 캐시 가능
- HTTP가 가진 캐싱기능 적용가능

### 4. Self-descriptiveness - 자체 표현 구조
- REST API 메시지만 보고도 이해할 수 있는 표현 구조로 되어있다.

### 5. Client-Server 구조
- REST 서버는 API를 제공하고, 
- 클라이언트는 사용자 인증이나  컨텍스트(session, 로그인 정보 등)을 직접 관리하는 구조로 구분된다.
- 때문에 서로 개발해야할 내용이 명확해지고 의존성이 줄어들게 된다.
  
### 6. 계층형 구조
- REST 서버는 다중 계층으로 구성될 수 있으며 보안, 로드 밸런싱, 암호화 계층을 추가할 수 있어 유연한 구조를 가질 수 있고 프록시, 게이트 웨이 같은 네트워크 기반의 중간매체를 사용할 수 있다.