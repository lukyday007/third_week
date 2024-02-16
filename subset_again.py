# # ver 1
# def backTrack(sta, arr, visited, N):
#     if len(arr) == N:
#         # shallow copy & deep copy
#         subset.append(sum(arr[:]))
#         return
#
#     for i in range(sta, len(lst)):
#         if not visited[i]:
#             visited[i] = True
#             arr.append(lst[i])
#             backTrack(i, arr, visited, N)
#             arr.pop()
#             visited[i] = False
#     else:
#         return
#
# for tc in range(1, int(input())+1):
#     lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
#     N, M = list(map(int, input().split()))
#     visited = [False] * len(lst)
#     subset = []
#     backTrack(0, [], visited, N)
#     if M in subset:
#         print(f"#{tc} 1")
#     else:
#         print(f"#{tc} 0")



# ver 2
def dfs(sta, N, M):
    global result
    if sum(arr) == M:
        if len(arr) == N:
            result += 1
            return
        else:
            return

    for i in range(sta, len(lst)):
        arr.append(lst[i])
        dfs(i+1, N, M)
        arr.pop()

for tc in range(1, int(input())+1):
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    N, M = list(map(int, input().split()))
    result = 0
    arr = []
    dfs(0, N, M)
    print(f"#{tc} {result}")



