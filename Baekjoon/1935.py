import sys

n = int(input())
s = input()
nums = [0]*n
for i in range(n):
    nums[i] = int(input())
stack=[]

for ch in s:
    if ch.isupper():
        stack.append(nums[ord(ch)-ord('A')])
    else:
        num2=stack.pop()
        num1=stack.pop()
        if ch=='+':
            stack.append(num1+num2)
        elif ch=='-':
            stack.append(num1-num2)
        elif ch=='/':
            stack.append(num1/num2)
        elif ch=='*':
            stack.append(num1*num2)
print(f"{stack[0]:.2f}")




# ret = []
# stack = []
# n = int(input())
# s = input()
# for i in range(len(s)-1):
#     if s[i] == '*':
#         ret.append(stack.pop()*stack.pop())
#     elif s[i] == '/':
#         num_1 = stack.pop()
#         num_2 = stack.pop()
#         ret.append(num_2/num_1)
#     elif s[i] == '+':
#         ret.append(stack.pop()+ret.pop())
#     elif s[i] == '-':
#         num_3 = ret.pop()
#         num_4 = ret.pop()
#         ret.append(num_4-num_3)
#     else:
#         if i>0 and s[i-1] != s[i]:
#             num = int(input().strip())

#         stack.append(num)
# print(stack)
# print(ret)