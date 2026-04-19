import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    heap = []
    for i in range(len(nums)):

        heapq.heappush(heap, -nums[i])
    final_heap = []
    for i in range(len(heap)):
        temp = -heapq.heappop(heap)
        final_heap.append(temp)

    return final_heap





# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
