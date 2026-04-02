class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Nested for loop is O(n^2) time complexity, O(1) space
        # We can use a hash table to achieve O(n) time complexity for O(n) space

        previously_seen = {}

        for i in range(len(nums)):
            difference = target-nums[i]
            if difference in previously_seen:
                first_index = previously_seen[difference]
                return [first_index, i]

            else:
                previously_seen[nums[i]] = i


        