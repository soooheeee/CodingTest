import sys
input = sys.stdin.readline

ret=[]

N,M = map(int,input().split())
li=list(map(int,input().split()))

#print(li)
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            sum=li[i]+li[j]+li[k]
            if sum <= M:
             ret.append(sum)
print(max(ret))