# no imports, cleaned up a bit
# learned what setdefault does. 
class Solution:
        def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

            freqs_to_words = {}

            for word in strs:
                freq_map = [0] * 26
                for ch in word:
                    freq_map[ord(ch) - ord('a')] += 1

                fmap = tuple(freq_map)  
                freqs_to_words.setdefault(fmap, []).append(word)
                
            return list(freqs_to_words.values())
                                                                                                                                                                                                