import sys
input=sys.stdin.readline

N, B = map(int, input().split())
s = ''
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while N:
    s += str(arr[N%B])
    N //= B

print(s[::-1])

# N, b = input().split()
# ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# N = N[::-1]
# ret = 0

# for i,n in enumerate(N): # i는 인덱스, n은 요소
#     ret += (int(b)**i)*(ary.index(n))
# print(ret)

#참고: https://velog.io/@wlrhkd49/%EB%B0%B1%EC%A4%80-11005-%EC%A7%84%EB%B2%95-%EB%B3%80%ED%99%98-2-Python