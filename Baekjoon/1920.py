# import sys
# input = sys.stdin.readline

# n = int(input())
# n_li = set(map(int,input().split()))

# m = int(input())
# m_li = list(map(int,input().split()))


# for num in m_li:
#     if num in n_li:
#         print('1')
#     else:
#         print('0')

# import sys
# input = sys.stdin.readline

# n = int(input())
# n_li = list(map(int,input().split()))

# m = int(input())
# m_li = list(map(int,input().split()))

# start = n_li[0]
# middle = (0+n) // 2
# end = n_li[-1]

# for i in range(n):
#     ret = m_li(i)
    

# import sys
# input = sys.stdin.readline

# n = int(input())
# n_li = sorted(map(int,input().split()))

# # print(n_li)

# m = int(input())
# m_li = list(map(int,input().split()))


# def location(low, high):
#     i = 0
#     i +=1

#     if low > high:
#         return 0
#     else:
#         mid = low+high // 2

#         if m_li[i] == n_li[mid]:
#             return mid
#         elif m_li[i] > n_li[mid]:
#             print(m_li[i])
#             return location(mid+1,high)
#         elif m_li[i] < n_li[mid]:
#             print(m_li[i])
#             return location(low, mid-1)
            
    
#     i+=1
# locationout = location(0,n-1)
# print(locationout)

# import sys
# input = sys.stdin.readline

# def binary_search(target, data):
#     start = 0
#     end = n - 1

#     if start > end:
#         return 0

#     else:
#         mid = (start + end) // 2

#         if data[mid] == target:
#             return True

#         elif data[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1

#     return False

# import sys
# input = sys.stdin.readline

# n = int(input())
# a = sorted(list(map(int, input().split())))

# m = int(input())
# a2 = list(map(int, input().split()))

# for i in a2:
#     if binary_search(i, a):
#         print(1)
#     else:
#         print(0)

import sys
input = sys.stdin.readline

def binary_search(n_li, x, start, end):
    if start > end:
        return False
    mid = ( start + end ) //2
    if n_li[mid] == x:
        return True
    elif n_li[mid] > x:
        return binary_search(n_li, x, start, mid-1)
    else:
        return binary_search(n_li, x, mid+1, end)

n = int(input())
n_li = sorted(map(int,input().split()))

m = int(input())
m_li = list(map(int,input().split()))

for m in m_li:
    if binary_search( n_li, m, 0, n-1):
        print(1)
    else:
        print(0)