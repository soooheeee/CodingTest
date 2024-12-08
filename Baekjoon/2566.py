import sys
input=sys.stdin.readline

A,B=[],[]
max_num=0
row_1=0
col_1=0

for i in range(9):
    row=list(map(int,input().split()))
    A.append(row)

for col in range(9):
    for row in range(9):
        if A[col][row] > max_num:
            max_num=A[col][row]
            row_1=row
            col_1=col
print(max_num)
print(col_1+1,row_1+1)










# A,B=[],[]

# for i in range(9):
#     row=list(map(int,input().split()))
#     A.append(row)
#     print(max(A[i]))
#     B.append(max(A[i]))
#     print(B)
#     num=max(B)
#     print(num)
#     print(max(B))
# for row in range(1):
#     for col in range(1):
        
#         # print(A[row][col])
#         if num in A[:][:]:
#             print(A.index(num))  
#         # print(A[1][0])
#         print(A)
