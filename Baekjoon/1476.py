import sys
input = sys.stdin.readline

# @Author: sohee
# @Description: 브루트포스
# 1. 세 가지 주기: E주기(15), S주기(28), M주기(19)
# performance: O(1), O(7980)이 최악의 복잡도이긴 하지만 O(1)로 간주
# referance: 
# E 주기 (15), S 주기 (28), **M 주기 (19)**는 서로소이며, 최소공배수는 15 * 28 * 19 = 7980

# 입력 받기
e, s, m = map(int, input().split())

# 초기 연도 설정
year = e  # `e`를 기준으로 시작하여 E 주기를 맞추며 탐색

while True:
    # 주기 조건을 확인하여 연도가 S, M 주기를 만족하는지 확인
    if (year - s) % 28 == 0 and (year - m) % 19 == 0:
        print(year)
        break
    year += 15  # E 주기인 15씩 증가시켜 조건을 다시 확인