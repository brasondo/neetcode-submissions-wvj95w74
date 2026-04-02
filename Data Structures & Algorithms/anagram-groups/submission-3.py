from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freqs_to_words = defaultdict(list)

        # O(n)
        for word in strs:
            
            # O(1) space here
            word_freq = [0]*26

            # O(k)
            for i in range(len(word)):
                index = ord(word[i]) - ord('a')
                word_freq[index] += 1
            
            # Dictionary keys can only be immutable
            # Lists are mutable so convert list representation to immutable tuple
            
            word_freq = tuple(word_freq)
            freqs_to_words[word_freq].append(word)
        return list(freqs_to_words.values())


        

