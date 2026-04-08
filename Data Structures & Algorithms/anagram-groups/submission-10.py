class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freq2words = {}

        for i in range(len(strs)):
            freq = [0] * 26
            for c in strs[i]:
                index = ord(c) - ord('a')
                freq[index] += 1
            
            if tuple(freq) not in freq2words:
                freq2words[tuple(freq)] = [strs[i]]
            else:
                freq2words[tuple(freq)].append(strs[i])
        
        res = []
        for val in freq2words.values():
            res.append(val)
        return res


        