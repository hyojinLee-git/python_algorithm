import heapq


def solution(scoville, k):
    count = 0
    heap = []
    for s in scoville:
        heapq.heappush(heap, s)
    try:
        while heap[0] < k:
            count += 1
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            new = first + (second * 2)
            heapq.heappush(heap, new)
    except:
        return -1

    return count