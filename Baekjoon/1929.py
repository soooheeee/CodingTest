# import sys
# input = sys.stdin.readline

# a , b =map(int, input().split())

# for i in range(a,b+1):
#   if i == 2:
#     print(i)
#   if i == 3:
#     print(i)
#   if i == 5:
#     print(i)
#   if i == 7:
#     print(i)
#   if i%2 == 0:
#     continue
#   if i%3 == 0:
#     continue
#   if i%5 == 0:
#     continue
#   if i%7 == 0:
#     continue
#   if i%i == 0:
#     continue
#   else:
#     print(i)

import sys
input = sys.stdin.readline

m,n = map(int,input().split())

for i in range(m, n+1):
  if i==1:
    continue
  for j in range(2, int(i**0.5)+1):
    if i%j ==0:
      break
  else:
    print(i)