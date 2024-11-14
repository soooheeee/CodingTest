import sys
input = sys.stdin.readline


formula = input()
stack=[]

# formula = input().split()

# print(formula[1])

for i in range(len(formula)-1):
    if formula[i] == '*':
        stack.append(i)
    
    elif formula[i] == '/':
        stack.append(i)

    elif formula[i] == '+':
        stack.append(i)

    elif formula[i] == '-':
        stack.append(i)
    elif formula[i] == '(':
        stack.append(i)
    elif formula[i] == ')':
        print(stack.pop())
    
    else:
        print(formula[i],end='')