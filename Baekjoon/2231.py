import sys
input = sys.stdin.readline

n = int(input()) 
li=[]
for i in range(1, n+1):  
    # li=list((map(int, str(i))))
    # print(li)
    num = sum((map(int, str(i)))) 
    num_sum = i + num  
   
    if num_sum == n:
        print(i)
        break
    if i == n: 
        print(0)


#소희 풀이
# sum=0
# li=[]
# N=int(input())
# # li.append((N//100))
# # li.append((N//10)%10)
# # li.append(N%10)
# # print(li)
# # n=len(N)
# for i in range(9):
#     for j in range(10):
#         for k in range(10):
#             sum=i+j+k+(100*i+10*j+k)
#             if N == sum:
#                 li.append(i)
#                 li.append(j)
#                 # li.append(k)
#                 break
# print(li)
# print(N)