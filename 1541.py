s=input().split('-')

#print(s)
for i in range(len(s)):
  if s[i].isdigit():
    s[i]=int(s[i])
  else:
    s[i]=s[i].split('+')
    for j in range(len(s[i])):
      s[i][j]=int(s[i][j])
    s[i]=sum(s[i])
#print(s)

answer=s[0]
for i in range(1,len(s)):
  answer-=s[i]
print(answer)


