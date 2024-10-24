import sys
input = sys.stdin.readline

# @Author: sohee
# @Description: DP를 이용
# 1. 왼쪽 위에서 시작하는 것과 왼쪽 밑에서 시작하는 것 2가지 경우를 고려
# 2. 같은 열은 선택하면 안되기 때문에 이 전 열에서 다른 행 1칸 앞 혹은 2칸 앞을 선택해서 max를 통해 이전 값들의 합들이 더 큰 경우를 선택
# performance: O(N)
# reference: https://choyoungjang.tistory.com/152

t = int(input())

for _ in range(t) :
    n = int(input())
    dp = [list(map(int,input().split())) for _ in range(2)]

    if n > 1 :
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
    for i in range(2,n) :
        dp[0][i] += max(dp[1][i-1],dp[1][i-2])
        dp[1][i] += max(dp[0][i-1],dp[0][i-2])

    print(max(dp[0][n-1],dp[1][n-1]))