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
# 위의 결과를 통해 isinstance는 상속의 관계에서도 적용된다는 것을 확인할 수 있다.