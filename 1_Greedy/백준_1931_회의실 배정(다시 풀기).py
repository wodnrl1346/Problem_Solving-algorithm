import sys
input = sys.stdin.readline

# 회의수
n = int(input())

# 각 회의 시작 시각, 끝나는 시각
table = []

for i in range(n):
    start, end = map(int, input().split())
    table.append([start, end])

# 끝나는 시간의 오름차순 정렬 -> 시작 시간의 오름차순 정렬
table = sorted(table, key=lambda x: (x[1], x[0]))

# 배정할 수 있는 회의실 개수
cnt = 0
# 이전 end
last_end = 0

for start, end in table:
    if(start >= last_end):
        cnt += 1
        last_end = end

print(cnt)
