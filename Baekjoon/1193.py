import sys
input=sys.stdin.readline


num = int(input())
line = 1

while num > line:
    num -= line
    line += 1
    
# 짝수일경우
if line % 2 == 0:
    a = num
    b = line - num + 1
# 홀수일경우
elif line % 2 == 1:
    a = line - num + 1
    b = num

print(f'{a}/{b}')


# 참고 했던 블로그: https://velog.io/@hwsa1004/%EB%B0%B1%EC%A4%80-1193%EB%B2%88-%EB%B6%84%EC%88%98%EC%B0%BE%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%92%80%EC%9D%B4