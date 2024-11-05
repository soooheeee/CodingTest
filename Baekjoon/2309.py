import sys
input = sys.stdin.readline

# @Author: sohee
# @Description: 브루트포스
# 1. 일곱 난쟁이들의 키의 합은 100임
# 2. 9명의 난쟁들 중에서 키의 합이 100인 2명의 난쟁이를 고름
# performance: O(N^3) , O(N^3)의 시간복잡도를 가지지만 N이 9이므로 다 해도 시간제한 안된다.
# referance: https://yabyab2.tistory.com/99 → 시간 복잡도 | 파이썬은 1초에 2000만 연산
# 방법1: 브루트 포스, 방법2: combinations, 방법3: 재귀

heights = [0] * 9  # 9명의 난쟁이 키를 저장할 리스트

for i in range(9):
    heights[i] = int(input())

# 오름차순 정렬하여 출력이 정렬된 형태가 되도록 함
heights = sorted(heights)
extra_sum = sum(heights) - 100  # 7명의 키의 합이 100이 되기 위해 제거할 두 명의 키 합

# 두 난쟁이의 키를 찾아 제거하기
first_fake = 0
second_fake = 0

for j in range(9):
    for k in range(j + 1, 9):
        if heights[j] + heights[k] == extra_sum:
            # 제거할 두 명의 키를 찾음
            first_fake = heights[j]
            second_fake = heights[k]
            break

# 찾은 두 명의 키를 리스트에서 제거
heights.remove(first_fake)
heights.remove(second_fake)

# 남은 7명의 키를 한 줄씩 출력
print(*heights, sep='\n')
