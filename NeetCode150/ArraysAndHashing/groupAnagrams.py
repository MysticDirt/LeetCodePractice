from collections import Counter
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = dict()
        l = list()
        for i in range(len(strs)):
            c = frozenset(Counter(strs[i]).items())
            if(c not in d):
                d[c] = len(l)
                l.append(list())
            l[d[c]].append(strs[i])
        return l
"""
4. Group Anagrams
	- tuples are immutable lists, frozensets are immutable sets
	- mutable types cant be hashed (lists, dicts, sets) but immutable ones can (tupes, frozensets)
	- I turned each word into a counter and then a frozen set, but it seems like just sorting the word is the way to go
	- frozenset -> counter -> string is O(n) complexity since each conversion is O(n) but sorting is O(n logn).
	- I do not know why it is faster (maybe test cases are too small to reflect the double conversion thing)
	- I made a dictionary to store the frozenset key and the index for the final list
		and then added the word to the list based on the index of the dictionary
	- However, it seems it is better to store the sorted word key as the key for the words itself, and then just convert dictionary to map
	- That is why sorted is faster, less accessing needed. But for large lists my way might be better
	- Finished in 26 minutes
"""