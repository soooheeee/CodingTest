# import sys
# input = sys.stdin.readline

# cnt = 0
# n = int(input())
# ret = n

# for i in range(n):
#   if ret != 2 and ret !=3:
#     ret-=1
#     cnt+=1

#     if ret % 3 == 0:
#       ret = ret // 3
#       cnt+=1
#       if ret == 1:
#         break
#     elif ret % 2 == 0:
#       ret = ret //2
#       cnt+=1
#       if ret == 1:
#         break
#   elif ret == 2 or ret ==3:
#     if ret % 3 == 0:
#       ret = ret // 3
#       cnt+=1
#       break
#     elif ret % 2 == 0:
#       ret = ret //2
#       cnt+=1
#       break

# print(cnt)  

import sys
input = sys.stdin.readline

x=int(input()) # 수 입력받기
d=[0]*(x+1) # 1-based
for i in range(2,x+1): # 2부터 x까지 반복
    d[i]=d[i-1]+1 # 1을 빼는 연산 -> 1회 진행
    if i%2==0: # 2로 나누어 떨어질 때, 2로 나누는 연산
        d[i]=min(d[i],d[i//2]+1)
    if i%3==0: # 3으로 나누어 떨어질 때, 3으로 나누는 연산
        d[i]=min(d[i],d[i//3]+1)
print(d[x])
