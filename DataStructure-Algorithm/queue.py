class LinearQueue:
    def __init__(self):
        self.front = -1
        self.rear = -1

    def create_queue(self, size):
        # python의 list는 null값이 들어갈 수 없기 때문에 0이 빈 값이라고 생각하자
        self.queue = list([0 for i in range(size)])

    def add(self, item):
        if self.isFull:
            print('배열이 꽉찼습니다')
        else:
            self.rear += 1
            self.queue[self.rear] = item
            print(self.queue)

    def remove(self):
        if self.isEmpty:
            print('배열이 비어있습니다')
        else:
            self.front += 1
            self.queue[self.front] = 0
            print(self.queue)

    def peek(self):
        return self.queue[self.rear]

    def isEmpty(self):
        if self.front == self.rear:
            return True
        return False

    def isFull(self):
        if self.rear == len(self.queue) - 1:
            return True
        return False


class CircularQueue:
    def __init__(self):
        self.front = -1
        self.rear = -1

    def create_queue(self, size):
        # python의 list는 null값이 들어갈 수 없기 때문에 0이 빈 값이라고 생각하자
        self.queue = list([0 for i in range(size)])
        print(len(self.queue))

    def add(self, item):
        if self.isFull:
            print('배열이 꽉찼습니다.')
        else:
            self.rear += 1
            if self.rear >= len(self.queue):
                self.rear %= len(self.queue)
            self.queue[self.rear] = item
        print(self.queue)
        print('front: {} rear: {}'.format(self.front, self.rear))

    def remove(self):
        if self.isEmpty:
            print('배열이 비었습니다.')
        else:
            self.front += 1
            if self.front >= len(self.front):
                self.front %= len(self.queue)
            self.queue[self.front] = 0
        print(self.queue)
        print('front: {} rear: {}'.format(self.front, self.rear))

    def peek(self):
        return self.queue[self.rear]

    def isEmpty(self):
        if self.front == self.rear:
            return True
        return False

    def isFull(self):
        if self.rear == len(self.queue) - 1:
            return True
        return False


queue = CircularQueue()
queue.create_queue(7)
queue.add(1)
queue.add(2)
queue.add(3)
queue.add(4)
queue.remove()
queue.add(5)
queue.add(6)
queue.add(7)
queue.add(8)
queue.isFull()
queue.isEmpty()
queue.remove()
queue.remove()
queue.remove()
queue.remove()
queue.remove()
queue.remove()
queue.isEmpty()
