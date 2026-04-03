# had to google how to get max from dictionary and remove from dictionary
# apparently same as list with max() and .pop()

# need to return key with max value DUH

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_to_freq = {}

        for i in range(len(nums)):
            if nums[i] not in num_to_freq:
                num_to_freq[nums[i]] = 1
            else:
                num_to_freq[nums[i]] += 1
        
        ans = []
        for i in range(k):
            ans.append(max(num_to_freq, key = lambda x: num_to_freq[x]))
            num_to_freq.pop(max(num_to_freq, key = lambda x: num_to_freq[x]))
        return ans

        