string=list(input())
bomb=input()

stack=[]
for i in range(len(string)):
  #print(stack)
  stack.append(string[i])
  if stack[-1]==bomb[-1]:
    temp=[]
    for j in range(len(bomb)):
      if stack!=[] and bomb[-1-j]==stack[-1]:
        temp.append(stack.pop())
      else:
        break
    if len(temp)==len(bomb):
      continue
    else:
      for j in range(len(temp)):
        stack.append(temp.pop())
if len(stack)==0:
  print('FRULA')
else:
  print(''.join(stack))