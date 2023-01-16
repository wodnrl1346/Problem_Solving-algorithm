# 얼음틀 크기
n, m = map(int, input().split())

# 얼음틀을 2차원 리스트로 저장
graph=[]
for i in range(n):
    graph.append(list(map(int, input().split())))

def dfs(x, y):
    # 주어진 범위를 벗어나면 종료
    if x<-1 or x>=n or y<=-1 or y>=m:
        return False
     
    # 현재 노드를 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문처리
        graph[x][y] = 1
        
        # 상하좌우가 0이면서 
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    
    return False
    
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
            
print(result)