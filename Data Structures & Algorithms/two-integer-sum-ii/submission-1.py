class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s, e = 0, len(numbers) - 1

        while s < e:
            curr = numbers[s] + numbers[e]

            if curr > target:
                e -= 1
            elif curr < target:
                s += 1
            else:
                return [s + 1, e + 1]