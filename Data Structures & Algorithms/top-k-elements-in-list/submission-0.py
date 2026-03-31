class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l = [[] for _ in range(len(nums) + 1)]
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        for n in d.keys():
            l[d[n]].append(n)
        final = []
        ln = len(nums) -1
        while(k > 0):
            for val in l[ln]:
                final.append(val)
                k -= 1
                if k == 0:
                    return final
            ln-=1
        return final
                
