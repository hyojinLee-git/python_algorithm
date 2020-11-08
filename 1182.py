import sys

n, s = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
#print(arr)


def recursion(l1, l2, arr):
    arr.append(l1)
    for i, x in enumerate(l2):
        recursion(l1 + [x], l2[i + 1:], arr)


def combination(l):
    result = []

    recursion([], l, result)
    return result[1:]


#print(combination(arr))
com=combination(arr)
cnt=0
for i in range(len(com)):
    if sum(com[i])==s:
        #print(sum(com[i]))
        cnt+=1
print(cnt)