import sys
input = sys.stdin.readline

n = int(input())    # 숫자의 개수

l = list(input())

total = 0
for i in range(n):
    total += int(l[i])

print(total)