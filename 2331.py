import sys

a, p = map(int, sys.stdin.readline().split())

lst = []
lst.append(a)
while True:
    num = []
    a = lst[-1]
    while a // 10 != 0:
        num.append(a % 10)
        a //= 10
    num.append(a)

    sum = 0
    for n in num:
        sum += n ** p

    if sum in lst:
        print(lst.index(sum))
        break
    lst.append(sum)