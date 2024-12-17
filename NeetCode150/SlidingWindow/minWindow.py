from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        minl = -1
        minr = 1000000
        ref = set(t)
        need = Counter(t)
        excess = dict()
        while r < len(s) or len(need) == 0:
            if len(need) > 0:
                if s[r] in ref:
                    if s[r] in need:
                        need[s[r]] -= 1
                        if need[s[r]] == 0:
                            need.pop(s[r])
                        #print("need found", s[r])
                    else:
                        if s[r] in excess:
                            excess[s[r]] += 1
                        else:
                            excess[s[r]] = 1
                        #print("excess found", s[r])
                    #print(need, excess)
                r += 1
            else:
                if s[l] in ref:
                    if s[l] in excess:
                        excess[s[l]] -= 1
                        if excess[s[l]] == 0:
                            excess.pop(s[l])
                        #print("excess lost", s[l])
                    else:
                        need[s[l]] = 1
                        #print("need lost", s[l])
                    #print("l",l)
                #print("check", l, r)
                if minr - minl > r - l:
                    #print("update", l, r)
                    minr = r
                    minl = l
                l += 1
            #print("r",r)
        if minr > len(s):
            return ""
        else:
            #print("return answer", minl, minr)
            return s[minl:minr]
                    

"""
5. Minimum Window Substring
Leetcode hard, took me about 2 hours
O(n) time complexity, O(n) space complexity
This time, the execution of the logic was harder than the logic itself
I got the logic down pretty simply:
- For this problem, we have to keep track of duplicates too. So we have to use counter dictionaries to keep track of the sliding window
- We also have to know if there are excess desired characters in the sliding window so we know we can remove those characters to keep the window to a minimum
- Lastly, I want to know whether the window satisfies it in O(1) time, so I used the strategy of deleting keys once they hit 0
- So I decided to use two dictionaries: need and excess
    - Need has the characters that my sliding window does not have that it needs to have to be a full substring
    - Excess has the characters that my sliding window has more than enough of, so if I bring the left pointer forward, I can lose those characters fine
- Ref is just a set of all characters so I dont add unneeded characters into need and excess
- When my right pointer encounters a character in the original substring, if the character is in need, it will subtract from need
- If it is not in need, it will add to excess
- Once need is empty, I check if it is the minimum and then start moving the left pointer
- If the left pointer encounters a character in the original substring, if the character is in excess, it will subtract from excess
- If it is not in excess, it will add to need, then start moving the right pointer again
The logic was not hard to figure out, but executing it was harder than anticipated
I originally tried to individually while loop the left pointer instead of having the one whole while loop iterate both pointers
But that introduced issues because it would iterate the left pointer by an additional 1 in most circumstances, but not all
Since I could not patchfix it, I eventually switched to just having it part of an if statement rather than a while loop
Then I got it to work
"""