class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement not in seen:
                seen[nums[i]] = i
            else: return [seen[complement], i]