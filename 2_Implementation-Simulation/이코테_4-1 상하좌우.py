# 공간의 크기 n
n = int(input())

# 시작 좌표
x, y = 1, 1

# 경로 계획을 저장할 변수
path = input().split()

for chr in path:
    if(chr == 'L'):
        y -= 1
        if(y == 0):
            y = 1
    elif(chr == 'R'):
        y += 1
        if(y == n+1):
            y = n
    elif(chr == 'U'):
        x -= 1
        if(x == 0):
            x = 1
    elif(chr == 'D'):
        x += 1
        if(x == n+1):
            x = n
        
print(x, y)