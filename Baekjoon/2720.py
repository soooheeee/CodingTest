import sys
input=sys.stdin.readline

changes = [25, 10, 5, 1] #쿼터, 다임, 니켈, 페니
T = int(input())

for _ in range(T) :
    cost = int(input())
    ret = []

    for i in changes :
        ret.append(cost // i) 
        cost = cost % i	
        
    print(*ret)