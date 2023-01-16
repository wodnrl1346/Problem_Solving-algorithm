import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

t = int(input())

def dfs(x, y):
    if x<0 or x>m-1 or y<0 or y>n-1:
        return False

    if graph[x][y] == 1:    # 배추가 있는 노드 일 때
        graph[x][y] = 0 # 방문처리

        dfs(x, y+1)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x-1, y)

        return True

    else:   # 배추가 없는 노드이거나 이미 방문한 경우
        return False    

for _ in range(t):

    # 가로길이, 세로길이, 배추가 심어진 위치의 개수
    m, n, k = map(int, input().split())

    # 0: 배추가 심어져있지 않음, 1: 배추가 심어져있음
    graph = [[0] * n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1

    cnt = 0
    for i in range(m):
        for j in range(n):
            if dfs(i, j) == True:
                cnt += 1

    print(cnt)