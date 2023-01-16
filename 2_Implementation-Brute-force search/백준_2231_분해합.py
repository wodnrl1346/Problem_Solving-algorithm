# 입력되는 정수 n, 생성자는 항상 n보다 작은 자연수이다
n = int(input())

result = 0

for m in range(1, n+1):
    num = list(map(int, str(m)))
    
    subtotal = m + sum(num)
    
    if(subtotal == n):
        result = m
        break
        
print(result)