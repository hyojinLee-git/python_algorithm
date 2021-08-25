a=input()
b=input()

def toArabian(num):
  dic={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
  number=0
  for n in range(len(num)-1):
    if num[n]=='C':
      if num[n+1]=='D' or num[n+1]=='M':
        number-=dic[num[n]]
      else:
        number+=dic[num[n]]
    elif num[n]=='I':
      if num[n+1]=='V' or num[n+1]=='X':
        number-=dic[num[n]]
      else:
        number+=dic[num[n]]
    elif num[n]=='X':
      if num[n+1]=='L' or num[n+1]=='C':
        number-=dic[num[n]]
      else:
        number+=dic[num[n]]
    else:
      number+=dic[num[n]]
  number+=dic[num[-1]]
  return number

def toRoman(num):
  num=str(num)
  roman=''
  dic={1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
  for n in range(len(num)):
    now=int(num[n])
    if now==4:
      roman=roman+dic[10**(len(num)-n-1)]+dic[5*10**(len(num)-n-1)]
    elif now==9:
      roman=roman+dic[10**(len(num)-n-1)]+dic[10**(len(num)-n)]
    elif 5<=now<9:
      roman=roman+dic[5*10**(len(num)-n-1)]+(dic[10**(len(num)-n-1)]*(now-5))
    elif 1<=now<4:
      roman+=dic[10**(len(num)-n-1)]*now
  return roman

sum=toArabian(a)+toArabian(b)
print(sum)
print(toRoman(sum))
