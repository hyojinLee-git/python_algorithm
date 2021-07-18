from collections import deque
#톱니바퀴
gear=[]
for _ in range(4):
  gear.append(deque(list(map(int,input()))))

k=int(input())  #회전 횟수


def rotate(num,op):
  global gear
  #시계방향
  if op==1:
    temp=gear[num].pop()
    gear[num].appendleft(temp)
  #반시계방향
  else:
    temp=gear[num].popleft()
    gear[num].append(temp)


def check_right(num):
  global gear_rotate
  #4 이상이면 종료
  if num+1>=4:
    return
  #현재 톱니바퀴가 회전할때
  if gear_rotate[num][0]:
    #회전 조건
    if gear[num][2]!=gear[num+1][6]:
      gear_rotate[num+1][0]=True
      gear_rotate[num+1][1]=-1*gear_rotate[num][1]
      return check_right(num+1)
    else:
      return

def check_left(num):
  global gear_rotate
  #0보다 작을 때 종료
  if num-1<0:
    return
  #현재 톱니 회전할 때
  if gear_rotate[num][0]:
    #회전 조건
    if gear[num-1][2]!=gear[num][6]:
      gear_rotate[num-1][0]=True
      gear_rotate[num-1][1]=-1*gear_rotate[num][1]
      return check_left(num-1)
    else:
      return

for _ in range(k):
  num,op=map(int,input().split())

  gear_rotate=[[False,op] for _ in range(4)]
  gear_rotate[num-1][0]=True

  #회전여부와 방향 검사
  check_left(num-1)
  check_right(num-1)

  #회전
  for i in range(4):
    if gear_rotate[i][0]:
      rotate(i,gear_rotate[i][1])

#점수 계산
sum=0
for i in range(4):
  if gear[i][0]==1:
    sum+=2**i
print(sum)

