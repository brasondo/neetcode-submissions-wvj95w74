from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:



        buckets = [[] for i in range(len(nums)+1)]
        freqs = Counter(nums)


        for num in freqs:
            count = freqs[num]
            buckets[count].append(num)

        res = []
        for i in range(len(buckets)-1, -1, -1):
            for j in range(len(buckets[i])):
                res.append(buckets[i][j])
                if len(res) == k:
                    return res

