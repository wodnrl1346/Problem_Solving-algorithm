import sys
input = sys.stdin.readline

s = list(input())

decision = [-1] * 26

alphabet = list('abcdefghijklmnopqrstuvwxyz')

for i in range(len(s)):
    for j in range(len(alphabet)):
        if decision[j] == -1:   # 아직 등장하지 않은 알파벳에 대해서
            if s[i] == alphabet[j]:
                decision[j] = i

print(*decision)