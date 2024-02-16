# # BFS
# from collections import deque
# def BFS(G, v):
#
#     n = len(G)  # 정점의 개수
#     visited = [False] * n
#     queue = deque([v])  # 큐를 생성하고 시작점 v 삽입
#     print(queue)
#
#     while queue:    #  큐가 비어있지 않는 경우
#         t = queue.popleft()     # 큐의 첫 번째 원소 반환
#         if not visited[t]:      # 방문되지 않으면
#             visited[t] = True   # 표시
#             visit(t)
#             for i in G[t]:      # t와 연결된 모든 정점들에 대해
#                 if not visited[i]:      # 방문하지 않으면
#                     queue.append(i)     # 큐에 넣기
#
# def visit(node):
#     print(f"Visited: {node}")
#
# G = [[1, 2],
#     [0, 3, 4],
#     [0, 4],
#     [1, 5],
#     [1, 2, 5],
#     [3, 4]]

# BFS(G, 0)

# Q = []
# visited = [0] *(V+1)
# v = 1
# Q.append(v)
# visited[v] = 1
# while Q:
#     v = Q.pop(0)
#     # V 인접 정점들 중 방문하지 않은 정점을 찾기
#     for w in G[v]:
#         if visited[w] == 0:
#             visited[w] = 1
#             Q.append(w)


'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

V, E = map(int, input().split())
arr = list(map(int, input().split()))

G = [[] for _ in range(V + 1)]
for i in range(0, E*2, 2):
    u, v = arr[i], arr[i + 1]
    G[u].append(v)
    G[v].append(u)


# 그래프 탐색
# 1. 그래프 정보(인접리스트)
# 2. DFS(스택), BFS(큐)
# 3. 방문정보를 저장하기 위해 저장소(정점 번호의 범위)
# 4. 출발점, 도착점 정보
D = [0] * (V + 1)   # 출발점에서 해당정점까지 최단 거리
P = [0] * (V + 1)   # 최단 경로 트리

Q = []
visited = [0] * (V + 1)  # 정점번호 1부터 V까지 사용
v = 1                   # 출발점

# 출발점을 큐에 삽입, 방문정보 표시
Q.append(v); print(v, end=' ')
visited[v] = 1
# 빈 큐가 아닐동안
while Q:
    v = Q.pop(0)
    # v의 인접정점(G[v])들 중에 방문하지 않은 정점(w)들 찾는다.
    # v ----> w
    for w in G[v]:
        if visited[w] == 0:
            visited[w] = 1; print(w, end=' ')
            Q.append(w)
            D[w] = D[v] + 1 # 출발점에 w까지의 최단거리가 확정
            P[w] = v        # 바로전에 방문한 정점 v 저장

print()
print(D[1:])
print(P[1:])





















