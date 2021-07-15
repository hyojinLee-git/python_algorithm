string = input()

min = len(string) * 2 -1

#이미 펠린드롬일 때
if len(string)%2==0:  #짝수
  if string[:len(string) // 2] == string[:len(string) // 2 - 1:-1] and min > len(string):
    min=len(string)
else:
  if string[:len(string) // 2] == string[:len(string) // 2:-1] and min > len(string):
    min=len(string)

for i in range(len(string) - 1, -1, -1):
    temp = ''
    temp = string + string[i::-1]
    #print(temp)
    if len(temp) % 2 == 0:
        if temp[:len(temp) // 2] == temp[:len(temp) // 2 - 1:-1] and min > len(temp):
            min = len(temp)
    else:
        if temp[:len(temp) // 2] == temp[:len(temp) // 2:-1] and min > len(temp):
            min = len(temp)

print(min)