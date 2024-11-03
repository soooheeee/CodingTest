import sys
input = sys.stdin.readline

N = int(input())
cnt = 0
ret = 666

while True:
    if '666' in str(ret):
        cnt += 1
    if cnt == N:
        break
    ret += 1
print(ret) 
