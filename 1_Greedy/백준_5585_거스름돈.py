# 물건의 금액(지불할 돈)
n = int(input())

# 거스름돈 = 1000-물건의 금액
n = 1000 - n

list = [500, 100, 50, 10, 5, 1]

count = 0

for i in list:
    if(n >= i):
        count += (n // i)
        n = n % i

        if(n == 0):
            break

print(count)