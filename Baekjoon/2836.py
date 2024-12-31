# import sys
# input = sys.stdin.readline
# cnt=0
# i=1
# N=int(input())
# while True:
#     i+=1

#     cnt=N%int(5*i)
#     print(cnt)
#     for j in range(1,N-cnt):
#         if (N-cnt)%(3*j) == 0:
#             print(j)
#             print(j+cnt) 
#             break

import sys
input = sys.stdin.readline

sum=0
li=[]
li_2=[]
N= int(input())

for i in range(N):
    for j in range(N):
        if N==5*j+3*i:
            # print(j,i)
            sum=j+i
            li.append(sum)
            li_2.append(sum)
        else:
            li.append(-1)
# print(li)
if max(li) > -1: # if in ~ 안에 -1이 있다면 그거 출력 이런식으로도 해도 ㄱㅊ
    print(min(li_2))
else:
    print(min(li))


# 간단한 코드    
# def sugar(n):
#   for i in range(n//5, -1, -1):
#     if (n - 5*i)%3==0:
#       return i + (n - 5*i) //3

#   return -1

# n= int(input())
# print(sugar(n))