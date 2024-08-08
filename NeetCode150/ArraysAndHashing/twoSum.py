from typing import List

class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		d = dict()
		for i in range(1, len(nums)):
			d[nums[i-1]] = i-1
			if(target - nums[i] in d):
				return {d[target - nums[i]], i}
"""
3. Two Sum
	- To make it less than O(n^2) time complexity, use a dictionary
	- Store key value pairs of number, index, and search for target - current number in the dictionary
"""