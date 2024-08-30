class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = dict()
        max_frequency = 0
        max_length = 0
        left = 0
        right = 0
        while right < len(s):
            count[s[right]] = count.get(s[right], 0) + 1
            max_frequency = max(max_frequency, count[s[right]])
            length = right - left + 1
            if length - max_frequency <= k:
                max_length = max(max_length, length)
                right += 1
            else:
                count[s[right]] -= 1
                count[s[left]] -= 1
                left += 1
        return max_length
            
"""
3. Longest Repeating Character Replacement
COMPLETE SOLUTION:
After watching the NeetCode video drawing part I came up with this
- This line: count[s[right]] = count.get(s[right], 0) + 1
    - This makes it so that we do not have to check if s[right] is in count before incrementing
- This algorithm counts the frequency of letters in the sliding window and then subtracts it by the total length
- Then checks if that quantity is less than k
- But we only have to use the max_frequency because the max_length will only happen when max_frequency is at its max
    - Since k is a constant
- So we do not have to find the max of the dictionary every time
- If the string is not valid (not enough replacements), then increase the left side of teh sliding window
- O(n) solution, took me 10 minutes after watching the video.
First attempt is below:
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        left = 0
        replace_index = -1
        replace = ""
        deck = k
        for i in range(1, len(s)):
            max_length = max(max_length, i - left)
            if s[i] == s[left]:
                #print(left, i, s[left], replace, deck, "continue")
                continue
            elif s[i] == replace:
                if deck == k:
                    replace_index = i
                if deck > 0:
                    deck -= 1
                else:
                    replace = s[left]
                    left = replace_index
                    replace_index = i
                    deck = k - 1
                #print(left, i, s[left], replace, deck, "replace")
            else:
                if replace == "":
                    replace = s[i]
                    replace_index = i
                    if deck <= 0:
                        left = i
                    else:
                        deck -= 1
                else:
                    deck = k - 1
                    left = i - 1
                    replace = s[i]
                    replace_index = i
                #print(left, i, s[left], replace, deck, "other")
        max_length = max(max_length, len(s) - left)
        return max_length

"""
3. Longest Repeating Character Replacement
INCOMPLETE SOLUTION
I spent an hour on this problem so far.
Essentially the goal was to:
- Keep track of the current consecutive character and the character we are replacing
- If we encounter the replacing character, decrement our deck (how many times we can replace) by 1
- If it is the current consecutive character, do nothing
- If we run out of our deck, move the left pointer forward to the first occurrence of the replacement character
- Keep track of the maximum length of the sliding window as we go down
- If we run into a different character, not the current consecutive nor the replacing character, reset everything from that point on
However, there is a flaw:
    - If the string is like ABBB, it will count AAAB but it will not go back and count BBBB. It does not replace characters behind.
    - A solution would be to go backwards but that is a lot of code
    - This only really needs to happen if we have some deck left and we reach the end of the string.
Since this a LeetCode medium, the problem should not have that much code to solve it, so I probably did the approach wrong.
So I decided to look at solutions.
Looks like the only difference is:
    - When they run out of replacements, they move the left pointer forward until they hit a character where they used a replacement
    - And then iterate over the next character
    - Also they keep a count of the values to figure out which character is the most frequent, and then replace the other ones
"""