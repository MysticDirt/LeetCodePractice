from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        beginning = dict()
        end = dict()
        maxnum = 0
        if(len(nums) == 0):
            return 0
        beginning[nums[0]] = nums[0]
        end[nums[0]] = nums[0]
        for i in range(1, len(nums)):
            if(nums[i] - 1 in end):
                if(nums[i] + 1 in beginning):
                    bnum = end[nums[i] - 1]
                    enum = beginning[nums[i] + 1]
                    beginning[bnum] = enum
                    end[enum] = bnum
                    beginning.pop(nums[i] + 1)
                    end.pop(nums[i] - 1)
                    if(enum - bnum) > maxnum:
                        maxnum = enum - bnum
                else:
                    bnum = end[nums[i] - 1]
                    beginning[bnum] = nums[i]
                    end[nums[i]] = bnum
                    end.pop(nums[i] - 1)
                    if(nums[i] - bnum) > maxnum:
                        maxnum = nums[i] - bnum
            elif(nums[i] + 1 in beginning):
                enum = beginning[nums[i] + 1]
                end[enum] = nums[i]
                beginning[nums[i]] = enum
                beginning.pop(nums[i] + 1)
                if(enum - nums[i]) > maxnum:
                        maxnum = enum - nums[i]
            else:
                beginning[nums[i]] = nums[i]
                end[nums[i]] = nums[i]
        return maxnum + 1

"""
9. Longest Consecutive sequence of integers
    - By far the hardest in this category
    - INCOMPLETE
    - Already went over 30 minutes (over an hour at this point) and I have 61/76
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
"""