# # # ver 1
# # def enQueue(item):
# #     global rear
# #     rear = (rear + 1) % (N + 1)
# #     Q[rear] = item
# #
# #
# # def deQueue():
# #     global front
# #     front = (front + 1) % (N + 1)
# #     return Q[front]
# #
# #
# # T = int(input())
# # for tc in range(1, T + 1):
# #     N, M = list(map(int, input().split()))
# #     # 원형 큐 배열 생성 - N + 1크기여야 함
# #     if 3 <= N + 1 <= 100:
# #         Q = [0] * (N + 1)
# #     front = rear = 0
# #     arr = list(map(int, input().split()))
# #
# #     # 입력받은 숫자들 원형 큐에 채우기
# #     for a in arr:
# #         enQueue(a)
# #
# #     for _ in range(M):
# #         tmp = deQueue()
# #         enQueue(tmp)
# #         # front 보다 한 칸 뒤가 처음 값
# #     print(f"#{tc} {Q[front + 1]}")
#
# def enQueue(item):
#     global rear
#     rear = (rear+1) % (N+1)
#     Q[rear]= item
#
# def enQueue2():
#     global rear
#     rear = (rear+1) % (N+1)
#
# def deQueue():
#     global front
#     front = (front+1) % (N+1)
#
# T = 1
# for tc in range(1, T+1):
#     N, M = list(map(int, input().split()))
#     # 원형 큐 배열 생성 - N + 1크기여야 함
#     Q = [0] * (N + 1)
#     front = rear = 0
#     arr = list(map(int, input().split()))
#     # 입력받은 숫자들 원형 큐에 채우기
#     for a in arr:
#         enQueue(a)
#     print(Q)
#     for _ in range(M):
#         print(f"front : {front}, rear : {rear}")
#         # print(Q)
#         deQueue()
#         print(f"front : {front}, rear : {rear}")
#         # print(Q)
#         enQueue2()
#         print(f"front : {front}, rear : {rear}")
#         print()
#     print(f"#{tc} {Q[(front + 1) % len(Q)]}")


def enQueue(item):
    global rear
    rear = (rear + 1) % (N + 1)
    Q[rear] = item

def deQueue():
    global front
    front = (front + 1) % (N + 1)
    return Q[front]

T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    # 원형 큐 배열 생성 - N + 1크기여야 함
    Q = [0] * (N + 1)
    front = rear = 0
    arr = list(map(int, input().split()))

    # 입력받은 숫자들 원형 큐에 채우기
    for a in arr:
        enQueue(a)

    for _ in range(M):
        tmp = deQueue()
        enQueue(tmp)
        # front 보다 한 칸 뒤가 처음 값 모드 연산 쓰기
    print(f"#{tc} {Q[(front + 1) % len(Q)]}")

