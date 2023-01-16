# ����Ʋ ũ��
n, m = map(int, input().split())

# ����Ʋ�� 2���� ����Ʈ�� ����
graph=[]
for i in range(n):
    graph.append(list(map(int, input().split())))

def dfs(x, y):
    # �־��� ������ ����� ����
    if x<-1 or x>=n or y<=-1 or y>=m:
        return False
     
    # ���� ��带 �湮���� �ʾҴٸ�
    if graph[x][y] == 0:
        # �ش� ��� �湮ó��
        graph[x][y] = 1
        
        # �����¿찡 0�̸鼭 
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