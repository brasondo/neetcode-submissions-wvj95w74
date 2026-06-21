from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        freqmap_2_words = defaultdict(list)


        for s in strs:
            freq_map = [0] * 26
            for c in s:
                freq_map[ord(c)-ord('a')] += 1

            freq_map = tuple(freq_map)
            freqmap_2_words[freq_map].append(s)
        
        res = []
        for value in freqmap_2_words.values():
            res.append(value)
        return res
        
