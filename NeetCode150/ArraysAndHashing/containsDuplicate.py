from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for number in nums:
            if(number in s):
                return True
            else:
                s.add(number)

"""
. Check for duplicates true or false
	- use sets
"""