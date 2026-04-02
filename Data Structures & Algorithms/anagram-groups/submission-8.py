# with imports, defaultdict, minimal code
class Solution:
        def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

            freqs_to_words = defaultdict(list)

            for word in strs:
                freq = [0] * 26
                for c in word:
                    freq[ord(c) - 97] += 1
                freqs_to_words[tuple(freq)].append(word)
            return list(freqs_to_words.values())
                                                                                                                                                                                                