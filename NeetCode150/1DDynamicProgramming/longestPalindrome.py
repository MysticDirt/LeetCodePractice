class Solution:
    def longestPalindrome(self, s: str) -> str:
        #Palindrome strategy: Find midpoint, and go out left and right
        #But we dont know where it is
        #So we start from the beginning
        #Cool thing about palindromes, if we have abababa
        #Then for the a to continue being a palindrome it has to mirror the first 2 characters
        #So we need a ba at the end again for ababababa
        #Or abcdcba loses palindromacy moving from d to c as the middle though
        #So how do we check for that, do we always have to check?
        #I guess ill assume so, and see if time limit checks me
        sub = ""
        for i in range(len(s)):
            j = 0
            while i-j in range(len(s)) and i+j in range(len(s)) and s[i-j] == s[i+j]:
                if 2*j+1 > len(sub):
                    #print(i,j)
                    sub = s[i-j:i+j+1]
                    #print(sub)
                j += 1
            j = 1
            while i + j in range(len(s)) and i-j+1 in range(len(s)) and s[i+j] == s[i-j+1]:
                if 2*j > len(sub):
                    #print(i,j)
                    sub = s[i-j+1:i+j+1]
                    #print(sub)
                j += 1
        return sub

"""
5. Longest Palindrome Substring
- This is honestly kinda a brute force approach. It checks each character and sees if there is a palindrome around it.
- It does this by seeing what characters are around it and expanding outward, so it is a little smarter about checking palindromes.
Time O(n^2), Space O(1)
I did not get time checked, but I'll watch the NeetCode video to see if there is a better solution
So the NeetCode video had the same solution, but it looks like there is something called Manacher's algorithm that is O(n) time O(n) space
But for interview purposes it looks very out of scope, so I will not worry about it for now
"""