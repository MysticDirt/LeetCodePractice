class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        left = 0
        seen = dict()
        seen[s[left]] = left
        max_length = 1
        right = 0
        for right in range(1, len(s)):
            max_length = max(max_length, right - left)
            if s[right] in seen:
                left = max(left, seen[s[right]] + 1)
            seen[s[right]] = right
        max_length = max(max_length, right+1 - left)
        return max_length

"""
2. Length of Longest Subtsring Without Repeating Characters
Apparently I already did this problem in C++ but I forgot how to do it, so I did it again in Python
O(n) time
Logic is relatively simple
- We need to keep track of where we last seen a character and its index, so we keep a dictionary
    with the character as the key and the index as its value
- Keep a max_length variable, and two pointers for a sliding window
    - Keep checking if the current substring is the max length
    - Increment the right for every loop
    - Change the left when:
        - We encounter a duplicate character
            - Then find out where its index is using the dictionary
            - Set the left pointer to the maximum of its current value or the dictionary index + 1
                - We max it because we do not want the pointer going backwards in case the duplicate character is before another one
    - Update the dictionary with any new characters we've seen
        Repeat characters should be replaced anyway
- Return max length at the end
Problem took me around 30 minutes
"""