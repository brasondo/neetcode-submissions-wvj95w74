class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashy = {}
        buckets = [[] for i in range(len(nums)+1)]
        
        for num in nums:
            hashy[num] = 1 + hashy.get(num, 0)
        for num, cnt in hashy.items():
            buckets[cnt].append(num)


        res = []

        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res)==k:
                    return res 

        
        print(buckets)

        