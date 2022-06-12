# Typescript

## 도입

-   typescript(이하 ts)는 정적 언어이다.
    > 여기서 정적언어란?
    >
    > '타입' 즉 **자료형을 컴파일 시에 결정하는 언어들**을 말합니다.
    > C, java 언어들 처럼 변수에 들어갈 값의 형태에 다라 자료형을 지정하고 컴파일 시에 자료형에 맞지 않은 값이 들어있으면 컴파일 에러가 발생합니다.
    >
    > 이를 통해 컴파일 시에 타입을 결정하기 때문에 **속도가 빠르고**, 타입 에러로 인한 문제점을 초기에 발견할 수 있어 **타입의 안정성**이 높습니다.

## 기본 타입

---

Javascript와 거의 동일한 데이터 타입을 지원하고 열거타입을 사용해 더 편리하게 사용할 수 있습니다.

> -   Boolean
> -   Number
> -   String
> -   Tuple
> -   Enum
> -   Any
> -   Void
> -   Null & Undefined
> -   Never
> -   Object
> -   Type Assertions

### Boolean

`참/거짓(true, false)` 값을 가지는 `boolean` 값입니다.

```typescript
let isDone: boolean = false;
```

### Number

ts의 모든 숫자는 부동 소수 값입니다. 이에 `number`라는 타입으로 쓰이고 16,10진수와 ES5에서 소개된 2진수, 8진수 리터럴도 지원합니다.

```typescript
let decimal: number = 6;
let hex: number = 0xf00d;
let binary;
```

### String

javascript와 동일하게 **큰 따옴표(")나 작은따옴표(')** 모두 문자열 데이터를 감싸는데 사용할 수 있습니다. 또한 **템플릿 문자열**(`${expr}`)을 사용하여 여러 줄에 걸쳐 문자열을 작성할 수 있습니다.

```typescript
// String
let color: string = "byte";
color = "red";

let fullName: string = `Bob Bobbington`;
let age: number = 13;
let sentence: string = `hello, my name is ${fullName}.
I'll be ${age + 1} years old next month`;
// 위와 동일한 코드
let sentence2: string =
    "Hello, my name is " +
    fullName +
    ".\n\n" +
    "I'll be " +
    (age + 1) +
    " years old next month.";
```

### Array

배열타입은 두가지 방법으로 쓸 수 있는데,

1. 배열 요소를 나타내는 타입 뒤에 `[]`
2. 제네릭 배열 타입 `Array<elemType>`

```typescript
// Array
// 1. 타입 뒤에 []
let list: number[] = [1, 2, 3];
// 2. 제네릭
let list2: Array<number> = [1, 2, 3];
```

### Tuple

튜플 타입은 요소의 타입과 개수가 고정된 배열을 표현합니다. 하지만 요소들의 타입이 모두 같을 필요는 없고 `number, string` 타입을 정의해놓은 순서대로 해당하는 타입의 값을 넣어야합니다.

```typescript
// Tuple
let x: [string, number];
x = ["hello", 10]; // Success
x = [10, "hello"]; // Error

console.log(x[0].substring(1));
console.log(x[1].substring(1)); // Error

x[3] = "word"; //Error 정해진 인덱스 외에 다른 인덱스에 있는 요소에 접근하면 오류가 발생합니다.
```

### Enum

열거형이라고 부르는 `enum`은 값의 집합에 더 나은 이름을 붙여줄 수 있습니다. 기본적으로 0부터 시작하여 원소의 번호를 매깁니다. 하지만 하나 또는 모든 값을 수동으로 설정하여 번호를 바꿀 수 있습니다.

```typescript
//Enum
enum Color {
    Red,
    Green,
    Blue,
}
let c: Color = Color.Green;
console.log(c); // Output = 1

enum Animal {
    Dog = 2,
    Cat,
    Giraffe,
}
let myPet: Animal = Animal.Dog;
console.log(myPet);

enum Subject {
    Math = 3,
    English = 14,
    Social = 5,
    Science = 98,
    Algorithm = 35,
}
let nextLecture: Subject = Subject.Math;
console.log(nextLecture);

enum Book {
    Math = 3,
    English = 14,
    Social,
    Science = 34,
    Algorithm,
}
let myLecture: number[] = [Book.Social, Book.Algorithm];
console.log(myLecture); // 오류가 날 것 같지만 지정이 되지 않은 원소들은 이전 원소의 값의 +1 값이 자동으로 부여됩니다.
```

`enum`의 유용한 기능 중에는 매겨진 값을 사용해 `enum` 멤버의 이름을 알아낼 수 있는 기능이 있습니다.

```typescript
enum Cooker {
    Ladle,
    Chopsticks = 3,
}
let myCooker: string = Cooker[3];
console.log(myCooker); // Output: Chopsticks
```

### Any

정적언어인 ts는 타입을 미리 지정해주어야하지만 프로그래밍하는 중에는 예측할 수 없는 값을 가진 변수를 만들어야하는 상황은 올 수 있습니다. 이 때에 사용하는 값이 바로 `any`타입입니다. javascript나 java에서 `Object`가 비슷한 역할을 할 수 있다고 볼 수 있습니다. 하지만 `Object`로 선언된 변수들은 실제로 메서드가 존재하더라도 임의로 호출할 수 없습니다. 또한 `Any`타입은 여러 다른 타입이 섞인 배열을 다루는 등의 타입의 일부만 알고 전체는 알지 못할 때 유용합니다.

```typescript
// Any
let notSure: any = 4;
notSure = "maybe a string instead";
notSure = false;

let notSure2: any = 5;
notSure2.ifItExists();
notSure2.toFixed();

let notSure3: Object = 3;
notSure3.toFixed(); //Error

let arr: any[] = [1, true, "free"];
list[1] = 100;
```
