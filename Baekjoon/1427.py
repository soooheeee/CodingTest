import sys
input = sys.stdin.readline
li=[]

N=input()

for i in range(len(N)-1):
    li.append(N[i])
# print(li)

li=sorted(li,reverse=True)
for j in range(len(N)-1):
    print(li[j],end='')

# li_2=[1,1,10,100,1000,10000,100000,1000000]
# li=[]
# r=[]
# N=input().split()
# print(N[0])
# print(len(N[0]))
# r=N[0:7]
# print(r)
# for i in range(len(N[0])):
#     li.append(N[i:1])
# print(li)
# # N_2=sorted(N,reverse=True)
# # print(N_2)
# # for i in range(len(N)):
# #     print(N[i])