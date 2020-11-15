# 스택(Stack)

## 개념
- 한쪽 끝에서만 자료를 넣고 뺄 수 있는 **LIFO(Last In First Out) 형식**의 자료 구조입니다.
  
## 연산
![stackimage](https://cdn.programiz.com/sites/tutorial2program/files/stack-operations.png)
- POP : 스택에서 **가장 위에 있는 항목을 제거**합니다.
- PUSH : item하나를 **스택의 가장 윗 부분에 추가**합니다.
- PEEK : 스택의 **가장 위에 있는 항목을 반환**합니다.

## 구현
- ``` python ```을 이용하여 사용하는 방법
```python
# Shortcut functions for Stack in Python
stack = []
stack.append(1) #push
stack.pop() #pop
stack[-1] #peek 

# 구현
class Solution:
    stack = []
    def pop(self):
        behind_data = self.stack[-1]
        del stack[-1]
        return behind_data

    def push(self, item):
        return self.stack.insert(-1, item)

    def peek(self):
        return self.stack[-1]

    def isEmpty(self):
        if len(stack) == 0:
            return True
        else:
            return False
```

## 사용
- UNDO(Ctrl + Z) 기능
- 역순 문자열 만들기
- 수식의 괄호 검사
- 수식 후위표기번 반환 등등 아주 많습니다.