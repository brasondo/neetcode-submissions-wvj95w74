class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        num2freq = {}

        for num in nums:
            if num in num2freq:
                num2freq[num] += 1
            else:
                num2freq[num] = 1


        ans = []
        for i in range(k):
            ans.append(max(num2freq, key = lambda x: num2freq[x]))
            num2freq.pop(max(num2freq, key = lambda x: num2freq[x]))
        return ans