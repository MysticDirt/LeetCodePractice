from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = set(nums)
        #used = set()
        #i_used = set()
        result = set()
        for i in range(len(nums)-1):
            for j in range(i + 1, len(nums)):
                nums_k = -1*(nums[i] + nums[j])
                if nums_k in s and (nums_k != nums[i] and nums_k != nums[j]):
                    thing = [nums[i], nums[j], nums_k]
                    thing.sort()
                    result.add(tuple(thing))
                    #used.add(nums_k)
        count = 0
        for num in nums:
            if num == 0:
                count += 1
            if(count >= 3):
                result.add((0,0,0))
                break
        return list(result)

"""
3. Three Sum
I struggled a lot on this one, took 45 minutes
Ended up coming up with a O(n^2) solution
I do not know if it can be faster
At first I tried a lot of checks (the (unused) used set and the i_used set) to see if I already used duplicate values
But eventually I gave up and sorted the lists and added them into a set
Since the lists are fixed sizes it is constant time complexity, so it still is O(n^2)
But it is bottom 5% in speed, so there must be a better solution

MOST COMMON SOLUTION:
First they sort the list
Then they do the same algorithm as twoSum, but setting an i, j, and k index
i is the "anchor," the first element
j is the left index, k is the right index
If they find a hit with target 0, then record it and increment both j and k
This is still an O(n^2) solution though

There are some solutions that handle 6 different combinations of numbers (all positive, 2 positive, etc) but
they all seeem like O(n^2) too. So I will keep my solution
"""