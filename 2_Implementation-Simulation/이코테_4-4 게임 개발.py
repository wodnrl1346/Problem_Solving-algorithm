# 맵의 세로크기:n, 맵의 가로크기:m
n, m = map(int, input().split())

# 칸의 좌표(x, y) 바라보는 방향 direction
x, y, direction = map(int, input().split())


array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화 
d = [[0]*m for _ in range(n)]
d[x][y] = 1

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽 방향으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
        
# simulation
cnt = 1
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 회전한 후 직진하였을 때 가지 않은 곳이어야 하고, 육지여야 count한다
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        # 이동 수행
        x = nx 
        y = ny
        cnt += 1
        turn_time = 0
        continue
    
    else:
        turn_time += 1
    
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        
        # 뒤로 갈 수 있으면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        
        else:
            break
        
        turn_time = 0
        
print(cnt)