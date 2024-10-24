import sys
input=sys.stdin.readline

word = input().upper().strip() # 모든 알파벳을 대문자로 변경하기
word_list = list(set(word)) # 중복허용x 

cnt = []
for i in word_list:
  count = word.count
  cnt.append(count(i))

if cnt.count(max(cnt)) > 1:
  print("?")

else:
  print(word_list[(cnt.index(max(cnt)))])