class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c=="(" or c=="{" or c=="[":
                stack.append(c)
            elif c==")":
                if not stack:
                    return False
                elif stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            elif c=="]":
                if not stack:
                    return False
                elif stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif c=="}":
                if not stack:
                    return False
                elif stack[-1] == "{":
                    stack.pop()
                else:
                    return False
        return not stack

"""
1. Is Valid Parenthesis
O(n), took me 10 minutes
Classic problem, seen it before for homework
But a better approach would be to make a dictionary for the matching pairs and check like that
and instead of 3 elifs, do one else, do the first if not stack check, then put the other 3 conditions (only works if no other characters)
"""