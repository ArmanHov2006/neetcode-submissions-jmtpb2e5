import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) > h:
            return -1
        elif len(piles) == h:
            return max(piles)
        else:
            s, e = 1, max(piles)
            while s < e:
                m = (s+e)//2
                total_hours = 0
                for pile in piles:
                    total_hours += math.ceil(pile/m)
                if h < total_hours:
                    s = m + 1
                else:
                    e = m
            return e
