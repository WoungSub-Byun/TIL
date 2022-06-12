// Boolean
let isDone: boolean = false;
let isGone: boolean = true;

// Number
let decimal: number = 6;
let hex: number = 0xf00d;
let binary: number = 0b1010;
let octal: number = 0o744;

// String
let color: string = "byte";
color = 'red';

let fullName: string = `Bob Bobbington`;
let age: number = 13;
let sentence: string = `hello, my name is ${fullName}.
I'll be ${age + 1} years old next month`;
// 위와 동일한 코드
let sentence2: string = "Hello, my name is " + fullName + ".\n\n" + "I'll be " + (age + 1) + " years old next month.";

// Array
// 1. 타입 뒤에 []
let list: number[] = [1,2,3];
// 2. 제네릭
let list2: Array<number> = [1,2,3];

// Tuple
let x: [string, number];
x = ["hello", 10]; // Success
x = [10, "hello"]; // Error

console.log(x[0].substring(1));
console.log(x[1].substring(1)); // Error

x[3] = "word"; //Error 정해진 인덱스 외에 다른 인덱스에 있는 요소에 접근하면 오류가 발생합니다.

//Enum
enum Color {Red, Green, Blue};
let c: Color = Color.Green;
console.log(c); // Output = 1

enum Animal { Dog = 2, Cat, Giraffe};
let myPet: Animal = Animal.Dog;
console.log(myPet);

enum Subject { Math = 3, English = 14, Social = 5, Science = 98, Algorithm = 35 };
let nextLecture: Subject = Subject.Math;
console.log(nextLecture)

enum Book { Math = 3, English = 14, Social, Science = 34, Algorithm };
let myLecture: number[] = [Book.Social, Book.Algorithm];
console.log(myLecture) // 오류가 날 것 같지만 지정이 되지 않은 원소들은 이전 원소의 값의 +1 값이 자동으로 부여됩니다.

enum Cooker { Ladle, Chopsticks = 3 };
let myCooker: string = Cooker[3];
console.log(myCooker) // Output: Chopsticks

// Any
let notSure: any = 4;
notSure = "maybe a string instead";
notSure = false;

let notSure2: any = 5;
notSure2.ifItExists();
notSure2.toFixed();

let notSure3: Object = 3;
notSure3.toFixed(); //Error

let arr: any[] = [1, true, 'free'];
list[1] = 100;
