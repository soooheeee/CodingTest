# import sys
# input = sys.stdin.readline

# dic = {}

# for _ in range (3):
#     num = int(input())
#     if num in dic.keys():
#         dic[num]+=1
#     else:
#         dic[num]=1
# for _ in range(3):
#     if dic[num]==3:
#         print(10000+num*1000)
#     elif dic[num]==2:

import sys
input = sys.stdin.readline

a,b,c = map(int,input().split())

if a==b==c:
    print(10000+a*1000)
elif a==b:
    print(1000+a*100)
elif a==c:
    print(1000+a*100)
elif b==c:
    print(1000+b*100)
else:
    print(max(a,b,c)*100)