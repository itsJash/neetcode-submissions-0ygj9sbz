import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    output = []
    temp = 0
    for i in range(len(heap)):
        temp = heapq.heappop(heap)
        output.append(temp)

    return output
# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
