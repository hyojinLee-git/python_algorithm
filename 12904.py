def cal1(string):
  return string[:-1]

def cal2(string):
  string=string[:-1]
  answer=''
  for i in range(len(string)-1,-1,-1):
    answer+=string[i]
  return answer

m=input()
n=input()


while n!=m:
  if len(n)==0:
    print(0)
    break
  if n[-1]=='A':
    n=cal1(n)
  else:
    n=cal2(n)
if n==m:
  print(1)