#Task 2 Balanced brackets
class Solution:
    def is_valid(self, s: str) -> bool:
        stack = list()
        brackets = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for el in s:
            if el in brackets:
                stack.append(el)
            elif len(stack) == 0 or el != brackets[stack.pop()]:
                return False
        return len(stack) == 0


a = Solution()
print(a.is_valid("([])"))
