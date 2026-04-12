class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        cntr = {}

        for num in nums:
            cntr[num] = 1 + cntr.get(num, 0)

        heap = []
        
        for key, val in cntr.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                heapq.heappushpop(heap, (val, key))
        print([h[1] for h in heap])
        return [h[1] for h in heap]
