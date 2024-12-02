import sys
input = sys.stdin.readline

li=[]

N,K = map(int,input().split())

for i in range(N):
    if N%(i+1)==0:
        li.append(i+1)
if len(li) < K:
    print(0)
else:
    print(li[K-1])