# for 문을 이용한 단순 구현
N, M, K = map(int, input().split())
Array = list(map(int, input().split()))

Array.sort()
first = Array[N-1]
secound = Array[N-2]

count = 0       # 큰 수의 법칙에 따른 결과

while True:
    for _ in range(K):
        count += first
        if M == 0:
            break
        M -= 1

    if M == 0:
        break

    count += secound
    M -= 1

print(count)

# 수학적 방법
n, m, k = map(int, input().split())
Array = list(map(int, input().split()))

Array.sort()
first = Array[n-1]
second = Array[n-2]

# 큰수가 더해지는 횟수
count = int(m / (k+1))*k
count += m % (k+1)

result = 0
result += (count) * first
result += (m-count) * second

print(result)