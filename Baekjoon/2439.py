import sys
input = sys.stdin.readline

N = int(input())

# for i in range (N):
#     for k in range(N-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

for i in range(1,N+1):
    print(" "*(N-i) + "*"*i)