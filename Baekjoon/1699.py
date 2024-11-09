import sys
input = sys.stdin.readline

n = int(input())
dp = [k for k in range(n+1)]

for i in range(1, n + 1):
    for j in range(1, i):
        if j*j > i:
            break
        if dp[i] > dp[i-j*j]+1:
            dp[i] = dp[i-j*j] + 1
print(dp[n])

# import sys
# input = sys.stdin.readline

# n = int(input())

# dp = [i for i in range(n + 1)]

# for j in range(1,n+1):
#   dp[j] = dp[j-(int(j**(1/2)))**2]+1

# print(dp)
# print(dp[-1])

# for i in range(2, number + 1):
#     for j in range(1, i + 1):
#         square = j * j
#         if square > i:
#             break

#         if dp[i] > dp[i - square] + 1:
#             dp[i] = dp[i - square] + 1

# print(dp[number])



# n = int(input())

# sum=0
# cnt = 0

# while True:
#   if n !=0 :
#     sum=int(n**(1/2))
#     n=n-(sum**2)
#     cnt +=1
#   else:
#     break
# print(cnt)
# print(753**(1/2))