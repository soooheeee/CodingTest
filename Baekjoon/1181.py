import sys
input = sys.stdin.readline

N=int(input())
li=[]

for i in range(N):
    x=input().strip()
    y=len(x)
    li.append([y,x])
li=sorted(li)

for j in range(N):
    if j==0 or li[j][1] != li[j-1][1]: # j==0 넣어주기
        print(li[j][1])
# for j in range(N):
#     li_len.append(len(li[j]))
# print(li_len)
# print(sorted(li_len))
        

#         그러나, 리스트의 첫 번째 원소(j == 0일 때)는 이전 원소가 없기 때문에, 이 조건만으로는 첫 번째 원소가 출력되지 않습니다. 만약 첫 번째 원소와 두 번째 원소가 같은 문자열이라면, 첫 번째 원소는 이전 원소와 비교할 수 없으므로 li[j][1] != li[j-1][1] 조건은 거짓이 됩니다. 따라서, 첫 번째 원소는 이 조건에 의해 출력되지 않게 됩니다.

# 이 문제를 해결하기 위해 j == 0 조건을 추가합니다. 이 조건은 반복문이 리스트의 첫 번째 원소를 처리할 때 항상 참이 되도록 보장합니다. 따라서, 리스트의 첫 번째 원소는 조건문을 통과하여 출력됩니다. or 연산자는 두 조건 중 하나라도 참이면 전체 조건문이 참이 되므로, 첫 번째 원소는 별도의 비교 없이 출력되고, 그 이후의 원소들은 이전 원소와 다를 때만 출력됩니다.

# 요약하면, j == 0을 추가하는 이유는 리스트의 첫 번째 원소를 올바르게 처리하고, 중복 제거 로직이 나머지 리스트에 영향을 받지 않도록 하기 위함입니다.