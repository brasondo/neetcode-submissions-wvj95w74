class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        chars_in_substring = set()
        length = 0 
        left = 0
        


        for right in range(len(s)):
            while s[right] in chars_in_substring:
                chars_in_substring.remove(s[left])
                left += 1
            chars_in_substring.add(s[right])
            length = max(length, right- left + 1)
        return length






        