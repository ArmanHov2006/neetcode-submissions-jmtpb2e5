from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        
        for s in strs:
            alp = [0] * 26
            for l in s:
                alp[ord(l) - ord('a')] += 1
            
            key = tuple(alp)
            
            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]
        
        return list(d.values())