import sys
input = sys.stdin.readline

num = int(input())

for i in range(num):
    for j in range(i+1):
        print("*",end="")
    print('')