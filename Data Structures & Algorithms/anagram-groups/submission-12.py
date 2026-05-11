from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freqs2words = defaultdict(list)
        for string in strs:
            freq = [0]*26
            for c in string:
                index = ord(c) - ord('a')
                freq[index] += 1

            freqs2words[tuple(freq)].append(string)
        
        return list(freqs2words.values())


        