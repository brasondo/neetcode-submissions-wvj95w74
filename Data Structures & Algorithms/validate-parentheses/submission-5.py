class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        bracks = {'}': '{', ']': '[', ')': '('}

        for c in s:
            if c in bracks and stack and stack[-1] == bracks[c]:
                stack.pop()
            else:
                stack.append(c)
        print(stack)
        if stack: 
            return False
        else:
            return True