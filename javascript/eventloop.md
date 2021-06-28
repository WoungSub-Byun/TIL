# Event Loop

오늘은 Javascript의 Event Loop에 대해서 알아보겠습니다.

Event Loop는 단일 스레드인 JS엔진을 멀티 스레드처럼 보이도록 할 수 있는 기능입니다.
이를 이해하기 위해서는 Javascript의 프로세스 처리에 대해서 알아야합니다.

## Javascript Engine
![jsengine](https://miro.medium.com/max/2048/1*4lHHyfEhVB0LnQ3HlhSs8g.png)

JS 엔진은 **Memory Heap**과 **Call stack**으로 이루어져있습니다.

### Memory Heap
- 메모리 할당이 이루어지는 곳
- 선언한 변수, 함수 등

### Call Stack
- 코드가 실행될 때 쌓이는 곳
- Stack(LIFO)형태로 쌓임

## Web API
**DOM, Ajax, Timeout** 등이 실행되는 JS 엔진이 아닙니다.

1. Callstack에 비동기 함수 쌓임
2. 해당 비동기 함수가 Web API 호출
3. WebAPI는 해당 함수를 Callback Queue에 삽입


## Callback Queue
- 비동기적으로 실행된 콜백함수가 보관되는 영역
- Queue(FIFO) 구조

그래서, Event Loop는 뭘 하는 거야?

## Event Loop
1. Callstack에서 동기적으로 처리되는 함수들이 모두 실행되어
2. Callstack이 비었다면
3. Callback Queue의 첫번째, 즉 가장 먼저 들어온 비동기 함수를 Callstack으로 삽입합니다.

**위 과정을 통해 단일 스레드로 동작하는 Javascript에서 멀티 스레드처럼 비동기 처리가 가능합니다!.**