class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            while not s[i].isalnum():
                i += 1
                if i >= j:
                    return True
            while not s[j].isalnum():
                j -= 1
                if i >= j:
                    return True
            if(s[i].lower() != s[j].lower()):
                #print(s[i], s[j])
                return False
            else:
                i += 1
                j -= 1
            
        return True

"""
1. Verify Palindromes
Pretty easy question, took 7 minutes
Seen it before
next time just add the conditional into the mini while loops too instead of making another if statement
"""