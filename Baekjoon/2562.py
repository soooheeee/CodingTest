import sys
input = sys.stdin.readline

max=0
li=[]

for i in range(9):
    num=int(input())
    if max<=num:   
        max=num
        li.append(max)
    else:
        li.append(num)
print(max)
print(li.index(max)+1)

# 마지막에 print(li.index(max))를 해서 출력값이랑 똑같이 나오지 않았다
# 즉, 8이 나와야 하는데 7이 나왔다 .
# +1을 하니 값이 제대로 나왔다.
# index의 값이 0부터 시작하니 +1을 해줘야 한다.