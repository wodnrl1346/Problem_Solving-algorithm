n = list(input())

# n의 요소들을 더하기 위한 변수
sum = 0

# 3의 배수인지를 판별하기 위해 각 자리수를 더한 sum을 구한다
for i in range(len(n)):
    sum += int(n[i])

# step1: n에 0이 없으면(정수 n을 섞어서 10의 배수를 만들 수 없다) -1을 출력한다
# step2: list n의 요소들을 모두 더한 결과가 3의 배수가 아니면 -1을 출력
# 어떤 숫자가 3의 배수가 되기 위해서는 모든 자리수를 더한 결과가 3의 배수가 되어야 한다.
if(('0' not in n) or ((sum % 3) != 0)):
    print('-1')

# 0을 찾아내고 내림차순으로 배열하기 위해서는 문자열 리스트를 정수 리스트로 바꾸어야 한다
for i in range(len(n)):
    n[i] = int(n[i])

# 0을 포함하고 있으면서 3의 배수인 경우에 구한다
# step3: 내림차순으로 정렬하면 0이 맨 뒤로 가게 되어 가장 큰 30의 배수를 만들 수 있다.
if(0 in n and (sum % 3) == 0):
    n.sort(reverse=True)

    for i in range(len(n)):
        print(n.pop(0), end ='')