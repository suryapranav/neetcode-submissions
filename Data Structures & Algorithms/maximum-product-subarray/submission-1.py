import math

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = cur_max = cur_min = nums[0]
        for n in nums[1:]:
            candidates = (n, n * cur_max, n * cur_min)
            cur_max, cur_min = max(candidates), min(candidates)
            res = max(cur_max, res)
        return res
