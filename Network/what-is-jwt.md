# JWT - JSON Web Token

---

![jwtimage](https://media.vlpt.us/images/denmark-choco/post/88612d26-c989-460a-93f2-64f11d9ff217/jwt_logo.png)

## 개념

---

JSON Web Token(JWT)는 웹 표준으로서 JSON객체를 사용해 두 개체 사이에서 가볍고, 자가 수용적인 방식으로 정보를 안전하게 전달해줍니다.

- **다양한 프로그래밍 언어에서 지원**
- **자가 수용적(self-contained)이다.**
  JWT는 필요한 모든 정보(token에 대한 기본정보, 전달할 정보, signature)를 자체적으로 가지고 있습니다.
- **쉽게 전달된다.**
  웹의 경우 HTTP Header에 넣어 전달하거나, URL의 파라미터로 전달하는 등 쉽게 전송할 수 있다.

## 사용

---

- 회원 인증
  - 유저가 로그인을 하면 **서버에서 유저의 정보를 기반으로 한 Access Token을 발급**해주고 이 후 **유저는 서버에 해당 Access Token을 포함하여 전달**합니다. **서버는 클라이언트에게서 요청을 받을 때마다 해당 token이 유효하고 인증되었는지 검증을하고 권한이 있는지 확인하여 작업을 처리**합니다.
  - 서버는 유저의 **세션을 따로 저장할 필요가 없기 때문에 서버 자원을 아낄 수 있다는 장점**이 있습니다.
- 정보 교류
  - 정보가 sign되있어서 정보가 조작되지 않았는지 검증할 수 있기 때문에 안전하게 정보를 교환할 수 있습니다.

## 구조

---

![jwtstructure](https://velopert.com/wp-content/uploads/2016/12/jwt.png)

### Header - 헤더

- typ
  - Token의 type을 지정 (ex. JWT 등)
- alg
  - 해싱 알고리즘을 지정 (ex. HMAC SHA256, RSA 등)
  - 해당 알고리즘은 토큰을 검증할 때 사용되는 signature부분에서 사용됨

### Payload - 정보

- 직접적인 정보가 들어있다.
- 정보의 한 조각 => 클레임(claim) - name:value의 한 쌍으로 구성

  - 클레임의 종류 - 등록된(registered) 클레임 - 공개 (public) 클레임 - 비공개 (private) 클레임
    > **등록된 클레임**
    >
    > - 토큰에 대한 정보들을 담기 위해 이미 정해진 클레임들 - iss - sub - aud - exp - nbf - iat - jti
    >   **공개 클레임**
    > - 충돌이 방지된, URI 형식의 클레임
    >   **비공개 클레임**
    > - 쿨라이언트 <-> 서버 간의 협의하에 사용되는 클레임 이름들
    > - 이름 중복으로 인한 충돌 주의

- payload 예제

```json
"iss" : "test.com",
"exp" : "123456789000",
"https://test.com": true,
"userId": "102827465538",
"username": "test"
```

- 해당 payload를 인코딩 하여 보냅니다.
  > `base64`로 인코딩할 경우 `=`문자가 붙을 수 있는데 이를 `base64`인코딩의 `padding`문자라고 부릅니다. 이는 url-safe하지 않기 때문에 제거해야합니다. 제거해도 디코딩 할 때 문제가 되지 않기때문에 꼭 **전부 지워** 주세요

### Signature - 서명

header의 인코딩 값과 payload의 인코딩 값을 합친 후 secret key로 해쉬하여 생성합니다.

- 생성 과정

  - header와 payload을 인코딩한 값 사이에 `.`을 넣어주고 합칩니다.
  - 합친 값을 해쉬합니다.
  - signature 완성!

- 이렇게 signature까지 만든 후에는 지금까지 구한 값들을 `.` 중간자로 다 합쳐주면 하나의 jwt 토큰이 완성됩니다.
  ex) ` eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ2ZWxvcGVydC5jb20iLCJleHAiOiIxNDg1MjcwMDAwMDAwIiwiaHR0cHM6Ly92ZWxvcGVydC5jb20vand0X2NsYWltcy9pc19hZG1pbiI6dHJ1ZSwidXNlcklkIjoiMTEwMjgzNzM3MjcxMDIiLCJ1c2VybmFtZSI6InZlbG9wZXJ0In0.WE5fMufM0NDSVGJ8cAolXGkyB5RmYwCto1pQwDIqo2w`
