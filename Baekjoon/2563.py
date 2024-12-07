# import sys
# input=sys.stdin.readline

# A,B=[],[]
# max_ret=0
# col_ret=0
# num=int(input())

# for _ in range(num):
#     row=list(map(int,input().split()))
#     A.append(row)

# for i in range(num-1):
#     for j in range(num-1):
#         B.append(A[j][0]) # 최댓값을 구하기 위함
#         # print(col_ret)
#         col_ret=A[i][0]
#         if col_ret != max_ret:
#             col_ret+=10
#             if col_ret > A[j+1][0]:
#                 print(A[j+1][0])
#     max_ret=max(B)

import sys
input = sys.stdin.readline

num = int(input())
arr = [[0] * 101 for _ in range(101)] 

for _ in range(num): 
    A, B = map(int, input().split())
    for i in range(A, A+10):
        for j in range(B, B+10):
            arr[i][j] = 1

ret = 0
for i in arr: 
    ret += sum(i)

print(ret) 