import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    r, s = input().split()  # r='3', s='ABC'
    r = int(r)  # r=3
    s = list(s) # s=['A','B', 'C']
    
    p = []

    for i in range(len(s)):
        p.append(s[i] * r)

    p_final = ''

    for j in range(len(p)):
        p_final += p[j]
    
    print(p_final)