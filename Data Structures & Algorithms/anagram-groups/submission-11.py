from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freqs2words = defaultdict(list)

        for string in strs:
            freq = [0] * 26

            for c in string:
                index = ord(c) - ord('a')
                freq[index] += 1
            
            freq = tuple(freq)
            if freq in freqs2words:
                freqs2words[freq].append(string)
            else:
                freqs2words[freq] = [string]
        
        res = []
        for key, item in freqs2words.items():
            res.append(item)
        return res



        