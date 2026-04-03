# Runs faster because max only computed once
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        num2freq = {}

        for num in nums:
            if num in num2freq:
                num2freq[num] += 1
            else:
                num2freq[num] = 1


        ans = []
        for _ in range(k):
            most = max(num2freq, key = lambda x: num2freq[x])
            ans.append(most)
            num2freq.pop(most)
        return ans