from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        buckets = [[] for i in range(len(nums)+1)]
        cnts = Counter(nums)


        for key, val in cnts.items():
            buckets[val].append(key)
        
        ans = []
        print(buckets)
        for i in range(len(buckets)-1, -1, -1):
            if buckets[i]:
                for num in buckets[i]:
                    ans.append(num)
                    if len(ans) == k:
                        return ans
            else:
                continue





        