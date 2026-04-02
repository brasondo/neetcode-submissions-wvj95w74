# Just implementing without defaultdict in the case of no imports
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freqs_to_words = {}

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

            if word_freq in freqs_to_words:
                freqs_to_words[word_freq].append(word)
            else:
                freqs_to_words[word_freq] = [word]
        return list(freqs_to_words.values())


        

