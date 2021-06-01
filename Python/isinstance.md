# Python isinstance()

Python을 주언어로 정하고 개발하면서 다양한 라이브러리들 소스코드를 까보는데 그때마다 자주보이는 내장함수인 `isinstance()`에 대해 알아보았다.

- isinstance()

  - Python의 Built-in Method
  - `def ininstance(x, A_tuple) -> bool`
  - parameter
    - 타입 검사할 인스턴스
    - 특정 클래스 / 데이터 타입
  - output
    - `bool`

  ```python
  class Animal:
      pass

  animal_instance = Animal()

  print("animal_instance-Animal: ", isinstance(animal_instance, Animal))
  # >>> animal_instance-Animal:  True

  class Monkey(Animal):
      pass

  monkey_instance = Monkey()

  print("monkey_instance-Monkey: ", isinstance(monkey_instance, Monkey))
  print("monkey_instance-Animal: ", isinstance(monkey_instance, Animal))
  # >>> monkey_instance-Monkey:  True
  # >>> monkey_instance-Animal:  True

  ```

  - 위의 결과를 통해 `isinstance()`는 상속의 관계에서도 적용된다는 것을 확인할 수 있다.
