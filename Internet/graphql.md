# GraphQL
---
![graphql](./../Image/graphql.svg)

GraphQL은 Graph Query Language로, 페이스북에서 만든 쿼리 언어입니다.

## 🙄 GraphQL이란?
GraphQL은 sql과 같이 쿼리 언어입니다. 하지만 둘은 활용 목적에서 큰 차이점을 가지고 있습니다.
> SQl과 GraphQL의 목적
>
> *SQL*
> - **데이터베이스 시스템**에 저장된 데이터를 효율적으로 가져오는 것
>
> *GraphQL*
> - **Web Client**가 데이터를 서버로부터 효율적으로 가져오는것

기존의 웹 애플리케이션 구동 방식으로는, sql의 문장은 주로 **백엔드 애플리케이션**에서 작성하고 호출합니다.
하지만 GraphQL의 문장은 주로 **클라이언트 시스템**에서 작성하고 호출합니다.

> Sql Query 예시
```sql
SELECT plot_id, species_id, sex, weight, ROUND(weight / 1000.0, 2) FROM surveys;
```
> GraphQL Query 예시
```graphql
{
    hero {
        name
        friends {
            name
        }
    }
}
```

## ✅ GraphQL의 특징

### 1️⃣ 특정 데이터베이스나 플랫폼에 종속적이지 않다.
- HTTP API가 특정 플랫폼에 종속적이지 않은 것처럼 GraphQL도 특정 플랫폼에 종속적이지 않습니다. 
* 심지어 네트워크 방식에도 종속적이지 않습니다.
> GraphQL은 주로 네트워크 레이어 L7의 **HTTP POST메서드**와 웹소켓 프로토콜을 활용합니다. 하지만 필요에 따라 **TCP/UDP**, **이더넷프레임**을 활용 할 수도 있습니다.

### **GraphQL Pipeline**

![graphql](./../Image/graphql-pipeline.png)

- GraphQL Query가 들어오게 되면 Parse, Validate와 같은 처리과정을 거친후 백엔드 애플리케이션에서 구현한 GraphQL Resolver를 통해 DB에서 데이터를 가져오고 이것을 JSON 형태로 반환합니다.

### 2️⃣ REST API의 문제점 해결
GraphQL을 만든 Facebook의 블로그에서는 

> *RESTful API로는 다양한 기종에서 필요한 정보들을 일일히 구현하는 것이 힘들다.*

라고 말합니다.
따라서 정보를 사용하는 측에서 원하는 대로 정보를 가져올 수 있고, 보다 편하게 정보를 수정할 수 있도록 하는 표준화된 쿼리 언어가 바로 GraphQL입니다.

## ✅ GraphQL의 구조

### Query/Mutation
GraphQL의 요청하는 쿼리문과 응답 내용의 구조는 거의 일치합니다.
- request Query
```graphql
{
    hero {
        name
    }
}
```
- response
```json
{
    "data": {
        "hero": {
            "name": "R2-D2"
        }
    }
}
```

### 스키마/타입(schema/type)
- 오브젝트 타입과 필드
```graphql
type Character {
    name: String!
    appearsIn: [Episode!]!
}
```
- 오브젝트 타입: Character
- 필드: name, appearsIn
- 스칼라 타입: String, ID, Int 등
- 느낌표(!): 필수 값을 의미(non-nullable)
- 대괄호([,]): 배열을 의미

## 리졸버(resolver)
GraphQL 쿼리문 파싱은 대부분의 GrahpQL라이브러리에서 처리하지만, GraphQL에서 데이터를 가져오는 구체적인 과정은 resolver에서 담당하고 이를 백엔드 개발자가 직접 구현해야합니다.

QraphQL쿼리에서는 **각각의 필드마다 함수가 하나씩 존재** 한다고 생각하면 됩니다. 이러한 각각의 함수를 **리졸버**(resolver)라고 합니다. 리졸버는 다음 **타입을 반환**합니다.

 만약 필드가 **스칼라 값이라면 실행이 종료**되지만, 필드의 타입이 **스칼라 타입이 아닌 우리가 정의한 타입이라면 해당 타입의 리졸버를 호출**하게 됩니다.

 이러한 리졸버의 호출은 DFS로 구현되있을거라 추측됩니다. 이것에서 Graph라는 단어를 쓴 이유가 있을 것이라 생각합니다.

 연쇄 리졸버 호출은 DBMS간의 관계에 대한 쿼리를 매우 쉽고 효율적으로 처리 할 수 있습니다.


 ## 인트로스펙션(introspection)
 ![gqlapolloide](./../Image/graphql-apollo-ide.png)
> Apollo Server 라이브러리 용 웹 IDE화면

기존 서버-클라이언트 협업 방식에서는 API 명세서를 주고 받는 절차가 반드시 필요합니다.

GraphQL에서는 RSETAPI 명세서 공유와 같은 문제를 해결하는 것이 바로 인트로스펙션 기능입니다.

GraphQL의 인트로스펙션은 서버 자체엇 현재 서버에 정의된 스키마의 실시간 정보를 공유할 수 있습니다.

## GraphQL 라이브러리
- [릴레이(Relay)](https://relay.dev/)
- [아폴로(Apollo GraphQL)](https://www.apollographql.com/)


## 정리

GrahpQL은 기존 REST API의 단점을 보완하는 성능적인 장점을 가지고 있습니다. 또한 RESTAPI에서는 Swagger와 같은 라이브러리를 사용해서 API 명세서를 공유하는 것이 최선이었지만 GraphQL에서는 이를 인트로스펙션으로 대체하여 프론트엔드와 백엔드간 협업이 더 쉬워질 것으로 생각됩니다. 그러나 비교적 프론트엔드쪽에 할일이 많아질것이라고 생각합니다.
