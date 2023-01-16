import sys
input = sys.stdin.readline
string = input().rstrip()

stack = []

for s in string:
    if s == '(':
        stack.append(s)

    else:
        if len(stack) !=0 and stack[-1] == '(':
            stack.pop()
        else:
            stack.append(s)

print(len(stack))