class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = [-1*s for s in stones]
        heapq.heapify(heap)

        while (len(heap) > 1):
            element1 = -1 * heapq.heappop(heap)
            element2 = -1 * heapq.heappop(heap)
            if element1 == element2:
                continue
            new_stone = -(element1 - element2)
            heapq.heappush(heap, new_stone)
        
        return -heap[0] if heap else 0



