import sys
input = sys.stdin.readline

# @Author: sohee
# @Description: 브루트 포스
# 1. 총 5가지의 도형의 경우를 다 계산하여 그 중 가장 큰 거 찾기
# performance: O(n*m)
# reference: https://pythontutor.com/render.html#mode=display

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]  # n개의 행을 가져와야 함

# 가능한 모든 테트로미노 모양
tets = [
    [(0, 1), (0, 2), (0, 3)], [(1, 0), (2, 0), (3, 0)],  # 1x4 형태 
    [(0, 1), (1, 0), (1, 1)],  # 2x2형태
    [(1, 0), (1, 1), (2, 1)], [(0, -1), (1, -1), (1, -2)],  # ㄹ자 (회전)
    [(1, 0), (1, -1), (2, -1)], [(0, 1), (1, 1), (1, 2)],  # ㄹ자 (대칭)
    [(1, 0), (2, 0), (2, 1)], [(0, 1), (0, 2), (1, 0)],  # ㄴ자 (회전)
    [(0, 1), (1, 1), (2, 1)], [(0, 1), (0, 2), (-1, 2)],
    [(1, 0), (2, 0), (2, -1)], [(0, 1), (0, 2), (1, 2)],  # ㄴ자 (대칭)
    [(1, 0), (2, 0), (0, 1)], [(1, 0), (1, 1), (1, 2)],
    [(1, 0), (1, 1), (1, -1)], [(1, 0), (1, 1), (2, 0)],  # ㅗ자(회전)
    [(0, -1), (1, 0), (0, 1)], [(0, 1), (-1, 1), (1, 1)]
]

# 테트로미노 모양을 배치하고 합을 계산하는 함수
def calc(i, j, tet):
    temp = arr[i][j]  # 시작 위치의 값 포함
    for di, dj in tet:
        ni, nj = i + di, j + dj
        # 그리드 범위를 벗어나면 0을 반환 (유효하지 않음)
        if 0 <= ni < n and 0 <= nj < m:
            temp += arr[ni][nj]
        else:
            return 0
    return temp

# 가능한 모든 테트로미노 모양을 배치해 최대 합 찾기
ans = 0
for i in range(n):
    for j in range(m):
        for tet in tets:
            temp = calc(i, j, tet)  # 현재 위치에서 가능한 모든 모양의 합 계산
            ans = max(temp, ans)

print(ans)
