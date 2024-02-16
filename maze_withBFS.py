# # ver 1
# N = 5
# maze = [
# [1,3,1,0,1],
# [1,0,1,0,1],
# [1,0,1,0,1],
# [1,0,1,0,1],
# [1,0,0,2,1]
# ]
# Q = []
# visited = [[0] * N for _ in range(N)]
# dr = [1, 0, -1, 0]
# dc = [0, 1, 0, -1]
# move = 0
#
# for r in range(N):
#     for c in range(N):
#         if maze[r][c] == 2:
#             x, y = r, c
# Q.append([])
# visited[x][y] = 1
# while 0 in visited:
#     # goal!
#     if maze[x][y] == 3:
#         break
#
#     move += 1
#
#     # 중심에서 상하좌우 이동
#     for i in range(4):
#         x += dr[i]
#         y += dc[i]
#         # 범위 제한
#         if x < 0 or x >= N or y < 0 or y >= N:
#             break
#         Q.append((x,y))

# def BFS(x, y):
#     Q.append((x, y))
#     visited[x][y] = 1
#     if x < 0 or x >= N or y < 0 or y >= N:
#         return
#
#     if maze[x][y] == 3:
#         return move
#
#     if maze[x][y] == 1:
#         return
#
#     if visited[x][y] != 0:
#         return


from collections import deque
def BFS(x, y):
    queue = deque([(x, y, 0)])

    while queue:
        cur_x, cur_y, move = queue.popleft()

        # 범위 체크
        if cur_x < 0 or cur_x >= N or cur_y < 0 or cur_y >= N:
            continue
        # Goal?
        if maze[cur_x][cur_y] == 3:
            return move-1
        # 벽 or 방문한 곳
        if maze[cur_x][cur_y] == 1 or visited[cur_x][cur_y]:
            continue

        visited[cur_x][cur_y] = 1  # 방문 표시

        for i in range(4):
            queue.append((cur_x + dr[i], cur_y + dc[i], move + 1))
            # queue.append((cur_x + 1, cur_y, move + 1))
            # queue.append((cur_x, cur_y - 1, move + 1))
            # queue.append((cur_x, cur_y + 1, move + 1))

    # 방문한 곳이 없으면
    return 0
for tc in range(1, int(input())+1):
    N = int(input())
    maze = [list(map(int, input().split())) for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    visited = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                result = BFS(r, c)
                break

    print(f"#{tc} {result}")


