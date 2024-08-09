from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        beginning = dict()
        end = dict()
        maxnum = 0
        if(len(nums) == 0):
            return 0
        d = set(nums)
        s = list(d)
        beginning[s[0]] = s[0]
        end[s[0]] = s[0]
        for i in range(1, len(s)):
            if(s[i] - 1 in end):
                if(s[i] + 1 in beginning):
                    bnum = end[s[i] - 1]
                    enum = beginning[s[i] + 1]
                    beginning[bnum] = enum
                    end[enum] = bnum
                    beginning.pop(s[i] + 1)
                    end.pop(s[i] - 1)
                    if(enum - bnum) > maxnum:
                        maxnum = enum - bnum
                else:
                    bnum = end[s[i] - 1]
                    beginning[bnum] = s[i]
                    end[s[i]] = bnum
                    end.pop(s[i] - 1)
                    if(s[i] - bnum) > maxnum:
                        maxnum = s[i] - bnum
            elif(s[i] + 1 in beginning):
                enum = beginning[s[i] + 1]
                end[enum] = s[i]
                beginning[s[i]] = enum
                beginning.pop(s[i] + 1)
                if(enum - s[i]) > maxnum:
                        maxnum = enum - s[i]
            else:
                beginning[s[i]] = s[i]
                end[s[i]] = s[i]
        #print(beginning, end)
        return maxnum + 1

"""
9. Longest Consecutive sequence of integers
    - By far the hardest in this category (because im trying to make it O(n))
    - INCOMPLETE
    - Already went over 30 minutes (over an hour at this point) and I have 61/76 test cases complete
    - Thought process is that there are 2 cases where we need to update the store of consecutive integers
        1. When the integer is right behind another integer (you find 1 after seeing 2 earlier in the list)
        2. When the integer is ahead of another integer (you find 3 after seeing 2 earlier in the list)
    - So for every integer we have to check if the number before or the number after it was there already
    - So we need good access time, so we use a dictionary (hashmap) for O(1)
    - Duplicate elements do not affect anything, so I decided to use a dictionary with the key as the start of a consecutive sequence
            and value as the end of a sequence
    - But this does not account for case 2, because we will not have O(1) access time for values, just keys
    - So we need another dictionary, that has the end integers as a key and the beginning of the sequence as a value
    - Then we have to update both if one gets a hit
    - Then we see which sequence has the biggest difference, and use that as the answer
    - Right now it checks maximum at every change of a sequence, but it would be faster to only check the dictionary at the end and iterate
            through the final key value pairs.
            That way it checks the maximum for less times with the same result
    - UPDATE: MOSTLY COMPLETE (4 testcases remaining)
    - I forgot to not add a new key value pair when the key already exists in the dictionary. So duplicate elements would create
        separate entries which would not combine if both were added to like 2-4 then 4-5
    - ISSUE:
    - It cannot detect duplicate values if the values are already in a range.
        If the dictionary has 6-9 then it wont detect 7 as being used, then it will add a new 7-7 entry
        Solution is to add a set that keeps track of every element we've seen. If we've seen it, skip it, if not, use it
        Or we can add everything into a set and then iterate through the set instead of a list
    - UPDATE: COMPLETE
    - That was the last issue
    - Although I did it inefficiently so that my previous code would still be compatible
    - I converted the list to the set and back to a list. 
    - Beat 47% in runtime and 6.71% in memory (I used a set and 2 dictionaries)
    - It was the same runtime as the sorting solutions, but if the testcases were bigger mine would be faster
    - Took me like 2 hours

    - MUCH BETTER SOLUTION:
        The easier but O(nlogn) solution is to turn it into a set, sort it, and then count consecutively
        But the best solution is to:
            - Turn it into a set
            - Keep a max count
            - While the set has numbers in it
                - Pop a number and store it into lets say n
                - Declare low as n-1
                - While low is in the set
                    - Remove it
                    - Decrement low by 1
                - Declare high as n+1
                - While high is in the set
                    - Remove it
                    - Increase by 1
                - If high-low-1 is higher than max count, make it the new max count
            - return max count
        - This is still O(n) because you are removing values in the small loops and it uses less space
        - The logic is less complicated too because instead of merging the counts you just count everything possible in the
            small loops
"""