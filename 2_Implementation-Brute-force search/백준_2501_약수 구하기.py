n, k = map(int, input().split())

# 약수
divisor_list = []

for i in range(1, n+1):
    if n % i == 0:
        divisor_list.append(i)

# N의 약수의 개수가 k보다 적어서 k번째 약수가 존재하지 않으면 0 출력
if(len(divisor_list) < k):
    print(0)

else:
    print(divisor_list[k-1])