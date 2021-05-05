import sys

n=int(sys.stdin.readline())
card=[]

_max=0
for _ in range(n):
  num=int(sys.stdin.readline())
  if abs(num)>_max:
    _max=abs(num)
  card.append(num)

count=[0]*(_max*2+1)

for i in range(len(card)):
  #음수는 0~max까지 저장
  count[card[i]+_max]+=1

print(count.index(max(count))-_max)

#메모리 에러ㅠㅠ
#sort 하고 count함수?