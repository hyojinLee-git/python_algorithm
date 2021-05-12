n,m=map(int,input().split())
deuddo=set()
bodo=set()
while n>0:
  n-=1
  deuddo.add(input())
while m>0:
  m-=1
  bodo.add(input())

hap=list(deuddo&bodo)
hap.sort()
print(len(hap))
for i in range(len(hap)):
  print(hap[i])