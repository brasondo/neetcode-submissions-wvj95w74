from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqs = Counter(nums)


        res = []
        for number, freq in freqs.items():
            res.append((freq,number))
        res.sort(reverse = True)
        

        ans = []
        for tup in res:
            ans.append(tup[1])
            if len(ans) == k:
                return ans




        