n, k = map(int, input().split())

data = []

for _ in range(n):
    data.append(int(input()))

# data list를 오름차순으로 정렬
data.sort(reverse=True)

count = 0

for i in data:
    if(k >= i):
        count += int(k/i)
        k = k % i

        if(k == 0):
            break

print(count)