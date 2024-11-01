import sys
input = sys.stdin.readline
from collections import deque

cursor_left_arr = deque(list(input().strip()))
cursor_right_arr = deque()
N = int(input())

# 명령어
for i in range(N):
    command = input().split()

    if command[0] == 'L':
        if len(cursor_left_arr) > 0:
            tmp = cursor_left_arr.pop()
            cursor_right_arr.appendleft(tmp)

    elif command[0] == 'D':
        if len(cursor_right_arr) > 0 :
            tmp = cursor_right_arr.popleft()
            cursor_left_arr.append(tmp)

    elif command[0] == 'B':
        if len(cursor_left_arr) > 0:
            cursor_left_arr.pop()
    else:
       cursor_left_arr.append(command[1])

print(''.join(cursor_left_arr) + ''.join(cursor_right_arr))
# 출처: https://dalseoin.tistory.com/entry/백준파이썬-1406-에디터 [Dalin's Archive:티스토리]



# left = list(input())
# right = []

# for _ in range(int(input())):
#     command = list(input().split())
#     if command[0] == 'L' and left:
#         right.append(left.pop())
#     elif command[0] == 'D' and right:
#         left.append(right.pop())
#     elif command[0] == 'B' and left:
#         left.pop()
#     elif command[0] == 'P':
#         left.append(command[1])

# answer = left + right[::-1]
# print(''.join(answer))

# string_list = list(input())
# cursor = len(string_list)

# for _ in range(int(input())):
#     command = list(input().split())
#     if command[0] == 'P':
#         string_list.insert(cursor, command[1])
#         cursor += 1
  
#     elif command[0] == 'L':
#         if cursor > 0:
#             cursor -= 1

#     elif command[0] =='D':
#         if cursor < len(string_list):
#             cursor += 1
  
#     else:
#         if cursor > 0:
#             string_list.remove(string_list[cursor-1])

# print(''.join(string_list))

# string=input()
# string_2=[]
# stack=[]

# for j in range(len(string)-1):
#     string_2.append(string[j])
# print(stack)

# for i in range(int(input())):
#     command=input().split()

#     if len(string_2) !=0:
#         if command[0] == 'B':
#             string_2.pop()
#         elif command[0] == 'P':
#             string_2.append(command[1]) 
#             print(command[1])
#         elif command[0] == 'L':
#             stack.append(string_2[-1])
#             string_2.pop()
#     elif len(string_2) == 0:
#         # if command[0] == 'B':
#         #     string_2.pop()
#         if command[0] == 'P':
#             string_2.append(command[1]) 
#             print(command[1])

# for k in range(len(stack)-1,0,-1):
#     string_2.append(stack[k])
 
# # print(stack[0:len(stack):1])
# print(stack)
# print(string_2)