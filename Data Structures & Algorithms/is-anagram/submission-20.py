class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        countS, countT = [0]*26, [0]*26

        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            countS[index] += 1

            index = ord(t[i]) - ord('a')
            countT[index] += 1

        return countS == countT

            