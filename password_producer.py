def enQueue(item):
    global rear
    rear += 1
    return Q[rear]
def deQueue():
    global front
    front += 1
    return Q[front]
def empty():
    return front == rear

tc_num = int(input())
arr = list(map(int, input().split()))

Q = [0] * (len(arr)+1)
front = rear = -1

for val in arr:
    enQueue(val)

num = 1
while Q[rear]:          # 마지막 값이 0이 아닐 때
    val = deQueue()     # 맨 앞에 있는 데이터 뽑기
    val -= num
    if val < 0:
        val = 0
    enQueue(val)
    num = num + 1 if num < 5 else 1
    # if num < 5:
    #     num += 1
    # else:
    #     num = 1

while not empty():      # front != rear 할 동안
    print(deQueue(), end=" ")

