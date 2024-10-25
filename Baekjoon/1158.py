import sys
input = sys.stdin.readline

# n,k = map(int,input().split())
# queue=[]

# for i in range(n):
#     queue.append(i)
# for j in range(1,n):
#     if j * 3 < n:
#         queue.insert()
# print(queue) 

n, k = map(int, input().split())

person = list(range(1, n + 1))
dead_person = []
index = 0

for i in range(n): 
    index += k - 1

    if index >= len(person):
        index %= len(person)

    dead_person.append(person.pop(index))
    
print("<", ", ".join(map(str, dead_person)), ">", sep= "")