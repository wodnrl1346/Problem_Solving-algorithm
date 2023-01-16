# n:여자 m:남자 k:인턴십
n, m, k = map(int, input().split())

# 만들어 질 수 있는 팀의 개수를 셀 변수
count = 0

# step1: 팀 결성을 먼저 한다
while True:
    if(n < 2 or m < 1):
        break

    n -= 2
    m -= 1
    count += 1

# step2: 팀 결성 이후 n과 m에 대하여 k명의 인원을 뺀다
# 이때 m을 먼저 뺴고, m이 0이 되면 n을 뺸다.
# n과 m 모두 0이 되면 팀을 해체(n=2, m=1)하고 위의 과정을 반복한다.

for i in range(k):
    if(n == 0 and m == 0):
        count -= 1
        n = 2
        m = 1

    if (n != 0 or m != 0):
        m -= 1
        if (m < 0):
            m = 0
            n -= 1

print(count)