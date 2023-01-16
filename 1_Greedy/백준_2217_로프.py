import sys
input = sys.stdin.readline

# 로프의 개수
n = int(input())

weight = []

for i in range(n):
    weight.append(int(input()))

weight.sort(reverse=True)

result = []

for k in range(1, n+1):
    result.append(weight[k-1]*k)

print(max(result))

"""
시간 초과 코드

루프를 선택하는 모든 경우에 대한 물체가 가질 수 있는 최대 중량을 구하고 거기서 최대값을 선택하였다.
"""
# import sys
# input = sys.stdin.readline
#
# # 로프의 개수
# n = int(input())
#
# weight = []
#
# for i in range(n):
#     weight.append(int(input()))
#
# weight.sort(reverse=True)
#
# result = []
#
# for k in range(1, n+1):
#     result.append(min(weight[0:k])*k)
#
# print(max(result))