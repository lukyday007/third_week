# ver 1
# N = 5
# # 1 은 벽, 0 은 통로
# # 2 에서 3 으로 갈 수 있으면
# maze = [['1', '3', '1', '0', '1'], ['1', '0', '1', '0', '1'], ['1', '0', '1', '0', '1'], ['1', '0', '1', '0', '1'], ['1', '0', '0', '2', '1']]
#
# flag  = True
# def find_pass(x, y):
#     global flag
#     # N x N 범위 체크
#     if -1 < x <= N-1 or -1 < y <= N-1:
#         if maze[x][y] == '3':
#             flag = True
#         elif maze[x][y] == '1':
#             flag = False
#         else:
#             if find_pass(x-1, y) == '0' or find_pass(x+1, y) == '0' or find_pass(x, y-1) == '0' or find_pass(x, y+1) == '0':
#                 flag = True
#     else:
#         flag = False
#
# x, y = N - 1, maze[N - 1].index('2')
# result = find_pass(x, y)
# if result != True:
#     print(0)
# else:
#     print(1)


# # ver 2
# for tc in range(1, int(input())+1):
#     N = int(input())
#     # 1 은 벽, 0 은 통로
#     # 2 에서 3 으로 갈 수 있으면
#     maze = [list(map(str, input())) for _ in range(N)]
#     visited = [[0]*(N) for _ in range(N)]
#
#     def find_pass(x, y, visited):
#         global flag
#         # N x N 범위 체크
#         if x < 0 or x >= N or y < 0 or y >= N:
#             return False
#         # goal 도착?
#         if maze[x][y] == '3':
#             return True
#         # 벽
#         if maze[x][y] == '1':
#             return False
#         # 방문했는지?
#         if visited[x][y] == 1:
#             return False
#
#         visited[x][y] = 1
#
#         if find_pass(x-1, y, visited) or find_pass(x+1, y, visited) or find_pass(x, y-1, visited) or find_pass(x, y+1, visited):
#             return True
#         return False
#
#     for r in range(N):
#         for c in range(N):
#             if maze[r][c] == '2':
#                 x, y = r, c
#     result = find_pass(x, y, visited)
#     if result != True:
#         print(f"#{tc} 0")
#     else:
#         print(f"#{tc} 1")




# ver 2
N = 5
maze = [
[1,3,1,0,1],
[1,0,1,0,1],
[1,0,1,0,1],
[1,0,1,0,1],
[1,0,0,2,1]
]
Q = []
visited = [[0] * N for _ in range(N)]
def BFS(x, y, move):
    # N x N 범위 체크
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    # goal 도착?
    if maze[x][y] == 3:
        return move
    # 벽
    if maze[x][y] == 1:
        return False
    # 방문했는지?
    if visited[x][y] == 1:
        return False

    visited[x][y] = 1

    if BFS(x-1, y, move+1) or BFS(x+1, y, move+1) or BFS(x, y-1, move+1) or BFS(x, y+1, move+1):
        return True
    return False

for r in range(N):
    for c in range(N):
        if maze[r][c] == 2:
            x, y = r, c
result = BFS(x, y, 0)
