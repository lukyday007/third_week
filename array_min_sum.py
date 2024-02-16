# 가지치기
def backtrack(k, add):
    global total
    # 길이에 맞는지 확인
    if len(add) == N:
        if sum(add) < total:
            total = sum(add)
        return
    # 중간 중간 add의 총 합이 total보다 높으면 바로 취소
    elif sum(add) > total:
        return

    else:
        for col in range(N):
            # bit로 행을 체크
            if bits[col] != 1:
                bits[col] = 1
                add.append(board[k][col])
                backtrack(k + 1, add)
                add.pop()
                bits[col] = 0

for tc in range(1, int(input())+ 1):
    N = int(input())
    board = [list(map(int, input().split()))for _ in range(N)]
    total = 21e8
    bits = [0] * N
    backtrack(0, [])
    print(f"#{tc} {total}")

# N = 3
# board = [
# [9, 4, 7],
# [8, 6, 5],
# [5, 3, 7]
# ]
# total = 10000
# bits = [0] * N
#
# def backtrack(k, add):
#     global total
#
#     if len(add) == N:
#         if sum(add) < total:
#             total = sum(add)
#         return
#     else:
#         for col in range(3):
#             if bits[col] != 1:
#                 bits[col] = 1
#                 add.append(board[k][col])
#                 backtrack(k + 1, add)
#                 add.pop()
#                 bits[col] = 0
# backtrack(0, [])
# print(total)






