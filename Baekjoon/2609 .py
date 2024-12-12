import sys
import math
input = sys.stdin.readline

a,b = map(int,input().split())

li_a=[]
s = 0
max = 0

if a>b:
    N = a%b
    print(N)
    math.lcm(a,b)
    

            
else:
    N=b%a
    print(N)
    math.lcm(a,b)
    
