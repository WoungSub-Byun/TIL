# OOP - Object Oriented Programming
---

요즘에는 대부분이 당연한 문법이라고 배우고 OOP로 개발하기 때문에 얼마나 획기적인 아이디어인지 모르지만, C와 같은 절차지향언어를 먼저 경험해본 사람들은 얼마나 신세계인 개념인지 느낄 것이다. 

절자 지향 프로그래밍(Procedual Programming)은 프로세스가 함수 단위로 순서대로 진행되는 것을 의미하는 반면 객체지향 프로그래밍(이하 OOP)는 *객체 들의 유기적인 관계를 통해* 프로세스가 진행된다.

## OOP
---
OOP는 프로그래밍 설계 패러다임 중 하나로, *현실 세계를 프로그램 설계에 반영한다는 개념*을 기반으로 접근하는 방법론이다. 

![oopimage](https://miro.medium.com/max/3200/1*fVKrjORLl2R8WVlvi23y4g.jpeg)



## OOP의 장단점

### 장점
- **유연성** -> 변경, 개발 및 보수 용이
- **직관적인 코드 분석 가능**
- **강한 응집력, 약한 결합력**

> 응집력? 결합력?
> - 응집력(cohesion)
> 
> *프로그램의 한 요소가 특정 목적을 위해 밀접하게 연관된 기능들이 모여서 구현되어 있고*, 지나치게 많은 일을 하지 않으면 그것을 응집력이 높다고 표현한다.
> - 결합력(coupling)
>
> 프로그램 코드의 한 요소가 다른 것과 얼마나 연결되어 있는지, 얼마나 의존적인지를 나타내는 정도 -> 결합력이 낮다는 것은 다른 요소들과 관계를 크게 맺고 있지 않고 덜 의존적이라는 것을 의미한다.

OOP는 하나의 문제해결을 위해 데이터를 모아 놓은 객체를 활용한 프로그래밍을 지향하므로 응집력을 강화하며, 클래스 간에 독립적으로 디자인함으로써 결합력을 약하게 할 수 있다.


## 기본 구성 요소

### Object - 객체
객체는 대상을 나타낸다.

구성요소 하나하나를 객체라고 한다.

ex) 사과, 원숭이, 의자 등등 

### Class
객체들이 공통적으로 갖는 속성(attribute)와 행위(method)를 정의한다.

OOP에서 코드 작성의 기본 단위이며 객체를 이루는 틀이라고 볼 수 있다.

다른 클래스와 독립적으로 디자인해야한다.

> Object to Class
붕어빵 - 객체
뿡어빵틀 - 객체를 생성하는 Class

### Method - 메서드
클래스로부터 생성된 객체를 사용하는 방법, 즉 객체들의 속성을 조작하는데 사용된다.

ex) 책상(object)을 든다. -> Method

## 💡특성

### 캡슐화 - Encapsulation
하나의 객체에 대해 그 객체가 특정한 목적을 위해 필요한 변수나 메소드를 하나로 묶는 것을 의미한다.

- **정보의 은닉화**
캡슐화를 하는 가장 중요한 이유가 여기에 있다. 만약 은행이라는 클래스에 잔고라는 변수가 public으로 지정되어있다면 외부에서 잔고 상태를 파악할 수 있고 메서드로 이를 바꿀 수도 있는 것이다. 따라서 데이터의 보안 성에 따라 private, protected 와 같은 접근 제한자를 잘 붙여 선언하고 getter, setter, property와 같은 메서드를 통해 간접적으로 접근가능하도록 한다.

```java
class BankBook {
    public int balance = 2000;
    public void changeBalance(int new_balance){
        self.balance = new_balance;
    }
}

```
- 이렇게 코딩한다면 자유롭게 접근 가능하여 보안성이 침해된다.
```java
class BankBook {
    private int balance = 2000;
    protected void balanceSetter(int new_balance){
        self.balance = new_balance;
    }
    protected int balanceGetter(){
        return self.balance
    }
}

```
- 위와 같이 setter, getter를 이용해 보안성을 강화한다.

### 추상화 - Abstraction
추상화는 객체들이 가진 공통의 특성들을 파악하고 불필요한 특성들을 제거하는 과정이다. 객체들이 가진 동작을 기준으로 메서드를 만드는데, 속성위주가 아닌 동작 위주로 작업 하는 것이 중요하다. 객체의 동작에 연관이 되지 않는 속서들은 격국은 불필요하기 때문에 동작을 먼저 정의하고 동작에 필요한 속성들을 정리하는 것이 좋다.
### 다형성 - Polymorphism
**같은 자료형에 여러 가지 객체를 대입하여 다양한 결과를 얻어내는 성질**을 말한다.
하나의 타입으로 다양한 결과를 얻을 수 있으며 객체를 부품화하기 때문에 **유지보수가 용이**하다.
주로 interface를 사용하여 다형성을 구현한다.
```java
interface Homework{
    void readingHw();
    void writingHw();
}
class AClass implements Homework {
    public void readingHw(){ //Overring
        System.out.println("운영체제 책 60P까지")
    }
    public void writingHw(){ //Overring
        System.out.println("java 다형성 interface로 구현")
    }
}

class BClass implements Homework {
    public void readingHw(){ //Overring
        System.out.println("자료구조 책 45P까지")
    }
    public void writingHw(){ //Overring
        System.out.println("java 상속 구현")
    }
}
public class TestCode01 {
    public static void main(String[] args){
        Homework hw1;
        hw1 = AClass();
        hw1.readingHw();
        hw1.writingHw();

        Homework hw2;
        hw2 = BClass();
        hw2.readingHw();
        hw2.writingHw();

    }
}
```
위의 코드처럼, 객체의 특성에 따라서 인터페이스르 통해 위와 같이 다양한 결과를 얻어낼 수 있다.

이것이 바로 **다형성**이다.
### 상속성 - Inheritance
OOP의 가장 큰 특성 중 하나가 바로 코드의 재사용성과 상속성이다. 같은 객체를 여러 개 만들어야 하는 경우, 한 번 작성된 코드를 활용하여 동일한 객체를 만들 수 있다.
```java
class A {
    String aField = "afield";
    public void Amethod(){
        System.out.println("Class A's Field: ", aField);
    }
}
class B extends A {
    public void Bmethod(){
        Amethod()
    }
}
```