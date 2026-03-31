class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = [0] * 26
        d2 = [0] * 26
        for l in s:
            d1[ord(l) - ord('a')] += 1
        for l in t:
            d2[ord(l) - ord('a')] += 1
        return d1 == d2