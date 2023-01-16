from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
graph = {
    0: [],
    1: [2, 3, 8],
    2: [1, 7],
    3: [1, 4, 5],
    4: [3, 5],
    5: [3, 4],
    6: [7],
    7: [2, 6, 8],
    8: [1, 7]
}

visited = [False] * 9

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
bfs(graph, 1, visited)
=======
bfs(graph, 1, visited)
>>>>>>> 3b8f165635d381cff00435d32a2794cff5cefcf1
=======
bfs(graph, 1, visited)
>>>>>>> 3b8f165635d381cff00435d32a2794cff5cefcf1
=======
bfs(graph, 1, visited)
>>>>>>> 3b8f165635d381cff00435d32a2794cff5cefcf1
