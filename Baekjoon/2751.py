# import sys
# input = sys.stdin.readline

# li=[]
# N=int(input())

# for _ in range(N):
#     li.append(int(input().strip()))
# for i in range(N):
#     for j in range(i,N):
#             if li[i]<li[j]:
#                 li[i],li[j]=li[j],li[i]
# for k in range(N):
#      print(li[k])

# 방법 2, 내장함수 사용하기

# import sys
# input = sys.stdin.readline

# li=[]
# sorted_li=[]
# N=int(input())

# for _ in range(N):
#     li.append(int(input().strip()))
# sorted_li=sorted(li)

# for k in range(N):
#      print(sorted_li[k])

# # 거꾸로
# li=[]
# sorted_li=[]
# N=int(input())

# for _ in range(N):
#     li.append(int(input().strip()))
# sorted_li=sorted(li,reverse=True)

# for k in range(N):
#      print(sorted_li[k])

# import io, os, sys
# from io import BytesIO, IOBase
 
# BUFSIZE = 8192

# class FastIO(IOBase):
#     newlines = 0
 
#     def __init__(self, file):
#         self._fd = file.fileno()
#         self.buffer = BytesIO()
#         self.writable = "x" in file.mode or "r" not in file.mode
#         self.write = self.buffer.write if self.writable else None
 
#     def read(self):
#         while True:
#             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
#             if not b:
#                 break
#             ptr = self.buffer.tell()
#             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
#         self.newlines = 0
#         return self.buffer.read()
 
#     def readline(self):
#         while self.newlines == 0:
#             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
#             self.newlines = b.count(b"\n") + (not b)
#             ptr = self.buffer.tell()
#             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
#         self.newlines -= 1
#         return self.buffer.readline()
 
#     def flush(self):
#         if self.writable:
#             os.write(self._fd, self.buffer.getvalue())
#             self.buffer.truncate(0), self.buffer.seek(0)
 
 
# class IOWrapper(IOBase):
#     def __init__(self, file):
#         self.buffer = FastIO(file)
#         self.flush = self.buffer.flush
#         self.writable = self.buffer.writable
#         self.write = lambda s: self.buffer.write(s.encode("ascii"))
#         self.read = lambda: self.buffer.read().decode("ascii")
#         self.readline = lambda: self.buffer.readline().decode("ascii")

# sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
# input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
# print = sys.stdout.write




n = int(input())
to_add = 1000000
cs = [0] * (to_add * 2 + 1)
for _ in range(n):
    cs[int(input()) + to_add] += 1
    
for i in range(to_add * 2 + 1):
    for _ in range(cs[i]):
        print(str(i - to_add) + '\n')

