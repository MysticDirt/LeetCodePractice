from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        reference = Counter(c for c in s1)
        need = len(reference)
        count = dict()
        left = 0
        right = 0
        while right < len(s2):
            if s2[right] in reference:
                if s2[right] in count:
                    count[s2[right]] += 1
                else:
                    count[s2[right]] = 1
                if count[s2[right]] > reference[s2[right]]:
                    need += 1
                while count[s2[right]] > reference[s2[right]]:
                    if s2[left] in count:
                        if count[s2[left]] == reference[s2[left]]:
                            need += 1
                        count[s2[left]] -= 1
                    left += 1
                if count[s2[right]] == reference[s2[right]]:
                    need -= 1
                if need == 0:
                    return True
            else:
                left = right + 1
                count.clear()
                need = len(reference)
            right += 1
        return False
        
"""
4. Permutation in String
Took me 30 minutes, O(m + n) time complexity
Where m is length of s1 and n is length of s2
The idea is to use a sliding window and keep track of the amount of each character in the sliding window
If it matches s1, then we found a permutation. Then we return true.
- reference is a Counter dictionary that keeps track of how many characters of which are in s1
- count counts the characters in the sliding window
- need keeps track of how many characters are left that have to match in count to find a permutation match
    - When need hits 0, we return True.
- When a character in s2 is not in s1 (not in reference), then reset everything and bring the left pointer to right.
- When a character is in s1, add one to the count.
    - If there is an overcount, bring the left pointer forward until the overcount is resolved
        - Decrement count and update need while doing so
        - Increment need so that decrementing need later will make it so that need remained the same
    - If the count matches the reference, decrement need by 1
- If true was not returned in the loop, return false.
"""