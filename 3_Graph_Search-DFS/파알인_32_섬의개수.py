# 육지:1, 물:0 일 때 섬의 개수를 계산
import sys
sys.setrecursionlimit(10**5)

# 가로:m, 세로:n
m, n = map(int, input().split())

graph = []

for i in range(m):
    graph.append(list(input()))

for i in range(m):
    for j in range(n):
        graph[i][j] = int(graph[i][j])

def dfs(x, y):
    if x<0 or x>m-1 or y<0 or y>n-1:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0     # 방문처리

        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x-1, y)
        return True

    else:
        return False

cnt = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:    # 탐색하지 않은 섬이 있을 때
            dfs(i, j)
            cnt+=1

print(cnt)