import sys
input = sys.stdin.readline

# n = int(input())
# ret =0
# arr = []
# li = list(map(int,input().split()))

# for i in li:
#   if i+ret <=0:
#     ret =0
#   ret += i
#   arr.append(ret)
# # print(arr)
# print(max(arr))

n = int(input())
m = list( map(int, input().split(' ')))
 
for i in range(1, n):
    m[i] = max(m[i], m[i] + m[i-1])
    
print(m)
print(max(m))