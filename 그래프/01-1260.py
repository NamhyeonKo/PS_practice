import sys
from collections import deque

# dfs를 재귀로 구현
def dfs(graph, v, visited):
    visited[v-1] = True
    print(v, end=' ')

    for i in graph[v-1]:
        if not visited[i-1]:
            dfs(graph, i, visited)

# bfs를 queue로 구현
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start-1] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v-1]:
            if not visited[i-1]:
                queue.append(i)
                visited[i-1] = True

N, M, V = map(int,sys.stdin.readline().split())

edge = [[] for _ in range(N)]
dfs_visited = [False] * N
bfs_visited = [False] * N

# 경로 저장
for i in range(M):
    start, end = map(int,sys.stdin.readline().split())
    edge[start-1].append(end)
    edge[end-1].append(start)   # 이건 방향그래프가 아니라 무방향 그래프이므로 해줘야함
# 출력 기준이 입력 기준x, 정점 번호가 작은 것o
for i in range(N):
    edge[i].sort()

# dfs 수행 결과 출력
dfs(edge,V,dfs_visited)
print()
# bfs 수행 결과 출력
bfs(edge,V,bfs_visited)