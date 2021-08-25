#세로: n,y,j
#가로: m,x,i

# 북0
#서3 동1
# 남2
n,m=map(int,input().split())
robot_y,robot_x,head=map(int,input().split())

graph=[]
for _ in range(n):
  graph.append(list(map(int,input().split())))


graph[robot_y][robot_x]=2

cnt=1
c=0
rotate=0
while True:
  #print('robot:',robot_y,robot_x,head)
  #print('rotate:',rotate)
  #print(graph)
  head-=1
  if head<0:
    head=3
  if head==0:
    robot_y-=1
    if graph[robot_y][robot_x]==0:
      rotate=0
      graph[robot_y][robot_x]=2
      cnt+=1
    else:
      robot_y+=1
      rotate+=1
      #head+=1
  elif head==1:

    robot_x+=1
    if graph[robot_y][robot_x]==0:
      rotate=0
      graph[robot_y][robot_x]=2
      cnt+=1
    else:
      robot_x-=1
      rotate+=1
      #head+=1
  elif head==2:
    robot_y+=1
    if graph[robot_y][robot_x]==0:
      rotate=0
      graph[robot_y][robot_x]=2
      cnt+=1
    else:
      robot_y-=1
      rotate+=1
      #head+=1
  elif head==3:
    robot_x-=1
    if graph[robot_y][robot_x]==0:
      rotate=0
      graph[robot_y][robot_x]=2
      cnt+=1
    else:
      robot_x+=1
      rotate+=1
      #head+=1

  #한바퀴 돌면
  if rotate==4:
    if head==0:
      #뒤로 한칸
      robot_y+=1
      if graph[robot_y][robot_x]==1:
        #뒤가 벽이면 break
        break
      else:
        rotate=0
    elif head==1:
      robot_x-=1
      if graph[robot_y][robot_x]==1:
        break
      else:
        rotate=0
    elif head==2:
      robot_y-=1
      if graph[robot_y][robot_x]==1:
        break
      else:
        rotate=0
    elif head==3:
      robot_x+=1
      if graph[robot_y][robot_x]==1:
        break
      else:
        rotate=0
#print(graph)
print(cnt)

