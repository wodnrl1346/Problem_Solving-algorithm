import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

# pensioner의 수: n, channel의 수: m, initial channel 번호: p
n, m, p = map(int, input().split())

graph = [[] for _ in range(m+1)]
for _ in range(n):
    a, b = map(int, input().split())    # 선호 채널: a, 비선호 채널:b
    graph[b].append(a)  # 입력된 채널을 비선호 하는 사람들의 선호하는 채널을 youngest 순서대로 저장한다.

visited = [False] * (m+1)   # loop가 만들어졌는지 판단하기 위한 방문처리 저장 리스트
cnt = 0     # 채널 변경 횟수

def dfs(v):
    global cnt  # 전역 변수로 선언
    visited[v] = True

    if graph[v]:    # 현재 채널을 비선호하는 사람이 있는 경우,
        next = graph[v][0]
        if not visited[next]:   # next channel에 방문하지 않았으면
            cnt += 1
            dfs(next)
        else:   # next channel에 방문했었다면, loop가 생긴 것이므로 -1을 출력한다.
            cnt = -1
            return

dfs(p)
print(cnt)