# import sys
# input=sys.stdin.readline

# cnt,ret=0,0

# A,B,V =map(int,input().split())

# while ret < V:
#     cnt+=1
#     ret+=A
#     if ret==V:
#         break
#     ret-=B
# print(cnt)

A, B, V = map(int, input().split())

x = (V-B)/(A-B)
if x == int(x): # 파이썬에서 나눗셈 결과는 기본적으로 float타입으로 반환되니깐, print 함수로 출력하면 소수점 이하의 숫자도 함께 출력됨
    print(int(x))
else:
    print(int(x) + 1)

   # 참고: https://blockdmask.tistory.com/524