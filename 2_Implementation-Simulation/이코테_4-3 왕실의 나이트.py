initial = list(input())

y = initial[0]
x = int(initial[1])

if(y == 'a'):
    y = 1
elif(y == 'b'):
    y = 2
elif(y == 'c'):
    y = 3
elif(y == 'd'):
    y = 4
elif(y == 'e'):
    y = 5
elif(y == 'f'):
    y = 6
elif(y == 'g'):
    y = 7
elif(y == 'h'):
    y = 8
    
# knight가 이동할 수 있는 경우의 수 count
cnt = 0

step=[(-1, 2), (1, 2), (-1, -2), (1, -2), (-2, -1), (-2, 1), (2, -1), (2, 1)]


for i, j in step:
    x_ = x + i
    y_ = y + j
    
    if((1 <= x_ <= 8) and (1 <= y_ <= 8)):
        cnt += 1
    
print(cnt)