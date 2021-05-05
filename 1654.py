import sys

k, n = map(int, sys.stdin.readline().rstrip().split())

wire = []
for _ in range(k):
    wire.append(int(sys.stdin.readline().rstrip()))

start = 1
end = max(wire)

result = []
while (start <= end):
    mid = (start + end) // 2
    num = 0
    for i in range(k):
        num += wire[i] // mid

    if num >= n:
        start = mid + 1
        result.append(mid)
    else:
        end = mid - 1

print(max(result))