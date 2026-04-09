class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        arr = []

        for num, freq in count.items():
            arr.append([freq, num])
        arr.sort(reverse=True)

        print(arr)
        res = []
        for i in range(k):
            res.append(arr[0][1])
            arr.pop(0)
        return res
        




        