class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)): return False
        d = dict()
        for c in s:
            if(c in d):
                d[c] += 1
            else:
                d[c] = 1
        for c in t:
            if(c not in d):
                return False
            elif(d[c] == 1):
                d.pop(c)
            else:
                d[c] -= 1
        return len(d) == 0
"""
2. Anagrams
	- Use map/dict, but python has a special dict called Counter which counts elements and stores it in a dictionary, use that
	- since its just a-z characters, you could use a straight up array rather than a dict and hash a to 0 and so on
"""