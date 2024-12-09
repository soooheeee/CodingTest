import sys
input = sys.stdin.readline

cnt=0
li=[]
for k in range(5):
    li.append(int(input().strip()))
    cnt+=li[k]

for i in range(5):
        for j in range(5):
            if i<j:
                if li[i] > li[j]:
                    # print(li[i],li[j])
                    li[i],li[j] = li[j],li[i]
print(cnt//5)
print(li[2])

#방법2, 내장함수로 문제풀기

# import sys
# input = sys.stdin.readline

# cnt=0
# li=[]
# for k in range(5):
#     li.append(int(input().strip()))
#     cnt+=li[k]

# sorted_li=sorted(li)
# print(sorted_li)
# print(cnt//5)
# print(li[2])