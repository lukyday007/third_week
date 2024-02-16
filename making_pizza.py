# ver 1
# oven, pizza = 3, 5
# cheese = [7, 2, 6, 5, 3]
#
# cook = []
#
# # [7, 2, 6]
# flag = True
# rear = 0
# cnt = 1
# while rear < len(cheese):
#     if flag:
#         for _ in range(oven):
#             cook.append(cheese[rear])
#             rear += 1
#         flag = False
#
#     print(f"{cnt} : {cook}")
#     for i in range(oven):
#         if cook[i] > 3:
#             cook[i] /= 2
#         else:
#             cook[i] -= 3
#             print(f"cheese : {cheese[rear]}")
#             cook[i] = cheese[rear]
#             rear += 1
#
#     print(f"{cnt} 조리 끝: {cook}")
#     cnt += 1
#     print()

# ver 2 원형 큐





def enqueue(item):
    global rear
    rear = (rear+1) % (limit+1)
    oven[rear] = item

def dequeue():
    global front
    front = (front + 1) % (limit+1)
    return oven[front]

def full():
    if (rear+1) % (limit+1) == front:
        return True
    return False

for tc in range(1, int(input())+1):

    limit, pizza = list(map(int, input().split()))
    cheese = list(map(int, input().split()))
    front = rear = 0
    oven = [0] * (limit+1)
    idx = 0
    finish = []
    while len(finish) != pizza:
        while True:
            if full() or idx == pizza:
                break
            enqueue([idx+1, cheese[idx]])
            idx += 1

        tmpIdx , che = dequeue()
        che //= 2
        if che != 0:
            enqueue([tmpIdx, che])
        else:
            finish.append(tmpIdx)

    print(f"#{tc} {finish[-1]}")




















