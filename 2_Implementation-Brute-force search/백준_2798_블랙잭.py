# 카드의 개수 n, 
n, m = map(int, input().split())

num = list(map(int, input().split()))

# 카드 3개에 적힌 수를 저장하는 리스트
check =[]

for i in range(n):
    for j in range(n):
        for k in range(n):
            # 카드를 겹치게 뽑지 않도록 만든다
            if i==j or i==k or j==k:
                continue
            
            # 카드를 겹치지 않게 뽑았으면, 세 수를 더한 결과가 m보다 작은 것들을 check 리스트에 저장한다.
            else:
                if(num[i]+num[j]+num[k] <= m):
                    check.append(num[i]+num[j]+num[k])

# 그 중 가장 큰 값을 출력한다.             
print(max(check))