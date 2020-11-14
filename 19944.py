n, m = map(int,input().split())

if n<m:
  print('TLE!')
else:
  if m==1 or m==2:
    print('NEWBIE!')
  else:
    print('OLDBIE!')