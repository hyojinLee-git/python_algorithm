import sys

n = int(input())

student = []

while n > 0:
    n -= 1
    name, k, e, m = sys.stdin.readline().split()
    k = int(k)
    e = int(e)
    m = int(m)
    student.append([name, k, e, m])

student.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for s in student:
    print(s[0])
