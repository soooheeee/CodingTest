import sys
input = sys.stdin.readline

for _ in range(int(input())):
    r,s = map(str,input().split())
    li=list(s)

    for i in range (len(li)):
        # li[i]=li[i]*int(r)
        print(li[i]*int(r) ,end='')
    print()
    
   
