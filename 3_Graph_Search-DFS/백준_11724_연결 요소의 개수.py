import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

# 노드의 개수, 간선의 개수
n, m = map(int, input().split())

# 각 노드에 인접해있는 노드를 2차원 리스트로 표현
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)       # 방문표시
cnt = 0                         # 연결 요소의 개수

def dfs(v):
    visited[v] = True
    
    for i in graph[v]:          # 1. 인접한 노드 이면서
        if not visited[i]:      # 2. 방문하지 않은 노드일 때
            dfs(i)

for j in range(1, n+1):
    if not visited[j]:
        dfs(j)
        cnt += 1

print(cnt)