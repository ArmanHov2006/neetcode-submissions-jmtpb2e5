from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            alphabet_list = [0] * 26
            for ch in s:
                alphabet_list[ord(ch) - ord('a')] += 1

            key = tuple(alphabet_list)

            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]

        return list(d.values())
