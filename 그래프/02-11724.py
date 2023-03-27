import sys

def DFS(graph,v,visited):
    visited[v-1] = True

    for i in graph[v-1]:
        if not visited[i-1]:
            DFS(graph,i,visited)

# 연결 요소의 개수가 dfs나 bfs와 같이 탐색 알고리즘으로 구했을 때
# 같은 집합이 되면 즉, 모든 정점을 방문하면 1개고,
# 아닌 경우에 남은 정점을 dfs로 탐색하면서 개수를 확인할 수 있다고 생각함.

N, M = map(int,sys.stdin.readline().split())

edge = [[] for _ in range(N)]
visited = [False] * N

for i in range(M):
    s, e = map(int,sys.stdin.readline().split())
    edge[s-1].append(e)
    edge[e-1].append(s) # 무방향 그래프 이므로..

cnt = 0

# 모든 정점이 방문될 때까지 반복문
while False in visited:
    i = visited.index(False) # 처음 시작점 찾기 (index함수 자체가 값인 것들 중 가장 앞의 값 가져옴)
    DFS(edge,i+1,visited) # index+1 (= vertex 값)을 시작으로 DFS
    cnt += 1 # 탐색 끝나면 해당 연결 요소 개수 증가

print(cnt)