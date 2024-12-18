#거꾸로 수 정렬하기

# import sys
# input = sys.stdin.readline

# li=[]

# N = int(input())
# for i in range(N):
#      li.append(input().strip('\n'))
# # print(li)
# # a=len(li)-1
# for j in range(len(li)-1,-1,-1):
#     # print(j)
#     print(li[j])
# # print(li)


#두 번째 방법, 내장함수 사용하기
# import sys
# input = sys.stdin.readline

# li=[]

# N = int(input())
# for i in range(N):
#      li.append(input().strip('\n'))
# li.reverse()
# # print(li)
# for j in range(N):
#      print(li[j])


import sys
input = sys.stdin.readline
# 입력을 받아 숫자로 변환하고 리스트에 추가
N = int(input())
li = []

for _ in range(N):
    li.append(int(input().strip()))

# 버블 정렬 알고리즘 구현
for i in range(N):
    for j in range(0, N-i-1):
        if li[j] > li[j+1]:
            li[j], li[j+1] = li[j+1], li[j]

# 정렬된 리스트 출력
for num in li:
    print(num)


#방법 2, 내장 함수 사용하기
    
# import sys

# N = int(input())
# li = []

# for _ in range(N):
#     li.append(int(input().strip()))

# li.sort()

# for num in li:
#     print(num)














# N = int(input())
# for i in range(N):
#     li.append(input().strip('\n'))
    
#     if i > 0:
#         for j in range(i+1):
#             print('/n',i,j)
#             if li[i-1] > li[i]:
#                 li[i-1],li[i]=li[i],li[i-1]
#             else:
#                 print('ddodododo',li[i-1],li[i])
                
# for k in range(N):
#     print(li[k])
# # print(li)