'''
6 5
1 4
1 3
2 3
2 5
4 6
1 6
'''


# 무향 그래프
def BFS(start):
    Q.append(start)
    visited[start] = 1

    while 0 in visited:
        start = Q.pop(0)
        for w in G[start]:
            if visited[w] == 0:
                visited[w] = 1
                Q.append(w)
                D[w] = D[start] + 1

for tc in range(1, 2):
    # 노드, 간선
    V, E = map(int, input().split())
    # 그래프 생성
    G = [[] for _ in range(V + 1)]
    # 그래프 입력
    for _ in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
    # 출발점에서 해당정점까지 최단 거리
    D = [0] * (V + 1)
    # 노드 시작점 넣고 빼는 큐 생성
    Q = []
    visited = [0] * (V + 1)  # 정점번호 1부터 V까지 사용
    start, goal = map(int, input().split())
    BFS(start)
    print(f"#{tc} {D[goal]}")
    print(f"D : {D}")















