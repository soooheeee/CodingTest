import sys
input = sys.stdin.readline

li=[]
sum=0
n=int(input())

li=list(map(int,input().split()))
max = li[0] 

for i in range (n):
    if max <=li[i]:
        max=li[i]
for j in range (n):
    change=li[j]/max*100
    sum+=change
avg=sum/n
# print(li)
# print(max)
print(avg)


# 두 번째 코드 
# 내장 함수 사용
N=int(input())
L=list(map(int,input().split()))
print(sum(L)/max(L)*100/N)