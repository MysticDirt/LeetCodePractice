from collections import defaultdict
from sortedcontainers import SortedDict
class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key in self.time_map:
            if timestamp in self.time_map[key]:
                return self.time_map[key][timestamp]
            else:
                i = (self.time_map[key]).bisect_left(timestamp) - 1
                if i >= 0:
                    return self.time_map[key].peekitem(i)[1]
        return ""

"""
6. Time Based Key Value Store
O(logn) set and get
I use a dictionary into sorted dictionaries
Sorted dictionaries are binary search trees under the hood, so they are O(logn) in access and insert
I was mainly inspred by C++ map which comes sorted by default
To set it I just add the value (libraries handle the data structure logic for me)
To get it, I first check if the value is there, if it is, bring it
If not, search for the item underneath it and bring it
- The flaw with this is that I do 2 searches per get whereas if I do it manually with my own binary search logic I only have to do 1
"""
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)