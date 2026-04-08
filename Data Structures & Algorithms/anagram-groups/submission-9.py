from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freq2words = defaultdict(list)

        for i in range(len(strs)):
            freq = [0] * 26
            for c in strs[i]:
                index = ord(c) - ord('a')
                freq[index] += 1
            
            freq2words[tuple(freq)].append(strs[i])
        
        res = []
        for val in freq2words.values():
            res.append(val)
        return res


        