import sys
sys.setrecursionlimit(10**5)

# 2에서 9까지 숫자가 주어졌을 때, 전화번호로 조합 가능한 모든 문자 출력
dic = {
    '2': "abc",
    '3': "def",
    '4': "ghi",
    '5': "jkl",
    '6': "mno",
    '7': "pqrs",
    '8': "tuv",
    '9': "wxyz"
}

digits = input()

result = []
def dfs(index, path):

    if len(path) == len(digits):
        result.append(path)
        return

    for i in range(index, len(digits)):    # 0, 1
        for j in dic[digits[i]]:    # 'abc', 'def'
            dfs(i+1, path+j)

# 예외 처리
if not digits:  # 아무것도 입력되지 않으면
    print([])

else:
    dfs(0, "")
    print(result)