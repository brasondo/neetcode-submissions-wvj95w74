# no imports
class Solution:
        def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
            freqs_to_words = {}
            for i in range(len(strs)):
                freq_map = [0] * 26
                word = strs[i]
                for j in range(len(word)):
                    index = ord(word[j]) - ord('a')
                    freq_map[index] += 1                                                                                          
                if tuple(freq_map) not in freqs_to_words:
                    freqs_to_words[tuple(freq_map)] = [word]
                else:
                    freqs_to_words[tuple(freq_map)].append(word)
            return list(freqs_to_words.values())
                                                                                                                                                                                                