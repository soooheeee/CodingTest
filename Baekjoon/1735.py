import sys
input = sys.stdin.readline
import math

a,b =map(int,input().split())
c,d=map(int,input().split())

max=math.gcd(b*d,(a*d)+(b*c))
bunmo=b*d//max
bunza=((a*d)+(b*c))//max
print(bunza,bunmo)
