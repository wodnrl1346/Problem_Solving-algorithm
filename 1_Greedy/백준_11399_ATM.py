# 줄을 서는 사람의 수
n = int(input())
# 줄을 서는 순서
p = list(map(int, input().split()))

# step1: 오름차순 정렬 -> 인출하는데 걸리는 시간이 최소가 될 수 있다
p.sort()

# 각 인덱스의 수를 누적해서 더한 결과를 저장할 리스트
partial = []

# 각 인덱스의 수를 누적해서 더한 결과
plus = 0

# step2: 부분합이 저장된 리스트를 만든다
for i in range(n):
    plus += p[i]
    partial.append(plus)

# step3: 부분합 리스트의 모든 요소를 더해서 정답을 출력한다
print(sum(partial))