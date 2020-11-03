# Queue
---

## 개념
먼저 집어 넣은 데이터가 먼저 나오는 **FIFO(First In First Out)구조**로 저장하는 방식

## 용어
- **Front** : 첫 번째 데이터
- **Rear** : 가장 마지막 데이터
  > **front, rear의 초깃값 : -1**


## 연산
---
- **FIFO** - First In First Out
- **Enqueue** : 데이터를 **삽입**하는 동작
  - **add(item)**  item을 리스트의 끝부분에 추가
    - ***rear = rear + 1 후 item 추가***
- **Dequeue** : 데이터를 **삭제**하는 동작
  - **remove** : 리스트의 첫 번째 항목을 제거
    - ***front = front + 1***
- **peek** : 큐에서 가장 위에 있는 항목을 반환
- **isEmpty** : 큐가 비어있을 때 true를 반환
  - ***(front == rear) ? True : False***
- **isFull** : ***rear = n - 1***

## 종류
 ### 선형
  ![linearqueueimage](./../Image/linearquueimage.png)
  - front와 rear의 값이 계속 증가하기 때문에 언젠가는 배열의 끝에 도달하게 되고 배열의 앞부분이 비어있더라도 사용하지 못한다.
 ### 환형
  ![]



## 구현
---

