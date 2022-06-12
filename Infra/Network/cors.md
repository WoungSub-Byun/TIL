# CORS (Cross Origin Resource Sharing)

---

웹을 개발한다면 한 번쯤은 들어보았을 CORS에 대해서 알아보겠습니다.

## 1️⃣ CORS란 무엇일까?

---

![corsimage](https://t1.daumcdn.net/cfile/tistory/256C904258CB85E01E)

- **CORS**: **C**ross **O**rigin **R**esource **S**haring
  **다른 출처로 리소스가 요청될 경우 브라우저에서 응답을 거부하는 정책**

> #### ❔ 출처

![urlimage](https://evan-moon.github.io/static/e25190005d12938c253cc72ca06777b1/6af66/uri-structure.png)

- 서버의 위치를 의미하는 URL들은 여러개의 구성 요소(protocol, host, path, query string, fragment)로 이루어져 있다.

즉, 서버가 접근을 허용한 출처(같은 출처)가 아닌 **접근을 허용하지 않은 출처(다른 출처)에서 요청할 경우 브라우저에서 보안상의 이유로 응답을 거부**하는 정책

## 2️⃣ 동작방식

---

기본적으로 웹 클라이언트가 서버에 리소스를 요청할 때는 HTTP프로토콜을 사용하여 요청을 보내는데, 이때 `Header`에 `Origin`이라는 필드에 출처를 함께 담아보내게 된다.

```
Origin: https://example.example.io
```

이후 서버가 이 요청에 대한 응답을 할 때 `Header`의 `Access-Control-Allow-Origin`이라는 값을 내려주고, 이후 `Response`를 받은 브라우저는 요청의 `Origin`과 `Response`의 `Access-Control-Allow-Origin`을 비교해본 후 유효한 응답인지 결정한다.

## 3️⃣ 해결방법

---

- 3가지의 해결방법이 있는데 이 중 우리는 서버에서 Access-Controll-Allow-Origin 헤더에 알맞은 값을 세팅해주는 법을 알아볼것이다.
- 이때, 와일드카드인 `*`를 사용하여 모든 출처를 받아들인다면 편하겠지만, 보안상으로 보았을 때 매우 심각한 이슈가 발생할 수 있으므로 가급적이면 출처를 명시해주도록 하자
- express, Django, Spring와 같이 유명한 백엔드 프레임워크에서는 CORS 세팅이나 middleware를 제공하고 있으니 손쉽게 설정이 가능하다.
  > **express에서 cors 라이브러리를 사용한 세팅 예시**

```javascript
var express = require("express");
const cors = require("cors");

var app = express();

// Set CORS middlware for all domain
app.use(cors());

//Set CORS middleware with options // limit origin only for livro-frontend server
const specificDomain = ""; // 접근 허용할 주소
const corsOptions = {
  origin: `http://${specificDomain}`,
  credentials: true,
};
app.use(cors(reactServerPath));
```
