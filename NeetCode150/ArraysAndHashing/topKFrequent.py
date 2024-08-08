from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums).most_common(k)
        result = list()
        for i in range(k):
            result.append(c[i][0])
        return result
"""
5. Top K Frequent elements
	- Easily solved with Counter and Counter.most_common() but in a real interview these might not be allowed
	- Took 3 minutes
	- Another solution made a dictionary, counted each number, sorted by value descending, then did it
"""