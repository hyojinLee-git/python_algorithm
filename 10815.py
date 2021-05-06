import sys

n = int(sys.stdin.readline().rstrip())
sang = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())
card = list(map(int, sys.stdin.readline().rstrip().split()))

answer = [0] * len(card)
sang.sort()


# 카드가 상근이꺼에 있는지 확인
def binary_search(array, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if target == array[mid]:
        return True
    elif target > array[mid]:
        start = mid + 1
        return binary_search(array, target, start, end)
    else:
        end = mid - 1
        return binary_search(array, target, start, end)


start = 0
end = n - 1
for c in range(m):
    if binary_search(sang, card[c], start, end):
        answer[c] = 1

for a in answer:
    print(a, end=' ')