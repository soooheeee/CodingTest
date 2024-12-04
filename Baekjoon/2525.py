import sys
input = sys.stdin.readline

H,M = map(int,input().split())
time = int(input())

# if time+M >= 60:
#     h=(time+M)//60
#     m=(time+M)%60
#     total_H = h+H
# else:
#     total_H=H
#     m=time+M
# if  total_H >23:
#     a=total_H-24
# else:
#     a=total_H
# if  m==60:
#     b=0
   
# else:
#     b=m
# print(a,b)

H, M = map(int, input().split())
T = int(input())
M += T
H = (H + M//60)%24
M= M%60
print(H, M)
