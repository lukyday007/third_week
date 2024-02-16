# # 큐
# q = [0] * 10
# front = rear = -1
#
# # euQueue(10)
# rear += 1
# q[rear] = 10
# rear += 1
# q[rear] = 20
# rear += 1
# q[rear] = 30
#
# while front != rear:    # 큐가 비어있지 않으면
#     front += 1          # deQueue()
#     print(q[front])


# 저장소
# 선형 큐
SIZE = 5
Q = [0] * SIZE
front = rear = -1

def enQueue(item):
    global rear
    # full 인지 확인
    if not rear == SIZE-1:
        rear += 1
        Q[rear] = item
    return

def deQueue():
    global front
    # empty 인지지 확인
    if not front == rear:
        front += 1
        return Q[front]
    return

# 원형 큐
SIZE = 5
Q = [0] * SIZE
front = rear = 0

def enQueue(item):
    global rear
    # full 인지 확인
    if not (rear+1) % SIZE == front:
        rear = (rear+1) % SIZE
        Q[rear] = item
    else:
        print('FULL')

def deQueue():
    global front
    # empty 인지지 확인
    if not front == rear:
        front = (front+1) % SIZE
        return Q[front]
    return

def empty():
    return front == rear

enQueue(1)
print(front, rear)
enQueue(2)
print(front, rear)
enQueue(3)
print(front, rear)
enQueue(4)
print(front, rear)
enQueue(5)
print(front, rear)
print(Q)

while not empty():
    print(deQueue())













