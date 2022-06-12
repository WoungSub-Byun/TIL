# API vs Library vs Framework
---

## API
**Application Programming Interface**
응용프로그램에서 운영 체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스

예를 들어, 맛집 공유 서비스를 개발하려고 하는데, 지도의 위치를 통해 맛집의 위치를 공유하려고 한다. 

하지만 지도 서비스 자체를 만드는것은 매우 비효율적이고 정확하지 않기 때문에 G사의 지도 서비스를 이용하려고 한다.
![apiimg](../Image/api.png)
- `/map/위도&경도`라는 url path를 사용하여 내 프로그램에서 G사의 지도 서비스에 요청을 보내면 해당 되는 정보를 G사에서 보내주게 된다.
- 이때 `/map/위도&경도`의 형식으로 리소스 측과 클라이언트 측이 연결되는 것을 바로 API라고 한다. 


**특징**
- 구현과 독립적으로 사양만 정의되어 있다.
- API에 따라 접근 권한이 필요할 수 있다.

## Library

**Library**

응용프로그램 개발을 위해 필요한 기능(함수)를 모아 놓은 소프트웨어

> 도서관에서는 내가 필요한 책을 가서 빌려서(대여하여) 읽을 수 있다. 이처럼 개발할 때 필요한 함수를 해당 함수가 미리 구현되어있는 라이브러리에서 호출하여 사용하는것을 말한다.



**특징**
- 독립성을 가진다.
- 응용프로그램이 *능동적*으로 라이브러리를 사용한다.

## Framework

응용프로그램이나 소프트웨어의 솔루션 개발을 수월하게 하기 위해 **제공된 소프트웨어 환경**

**특징**
- 응용프로그램이 *수동적*으로 프레임워크에 의해 사용된다.
- 클래스와 인터페이스의 집합
> ex) Spring Framework, Django, 



> ✔🟠 **API vs Library**
>**구현 로직의 유무**
    - O - Library
    - X - API

> ✔🟢 **Library vs Framework**
>**흐름 주도권을 누가 가지고 있나**

![lifr](https://www.programcreek.com/wp-content/uploads/2011/09/framework-vs-library.png?ezimgfmt=rs:400x180/rscb8/ng:webp/ngcb8)