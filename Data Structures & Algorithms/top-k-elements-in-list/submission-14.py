from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        cntr = Counter(nums)    

            
        heap = []
        for key, val in cntr.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                heapq.heappushpop(heap, (val, key))

        res = [h[1] for h in heap]
        return res
        
        