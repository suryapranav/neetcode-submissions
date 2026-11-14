class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = [1] * (len(nums))
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    arr[i] = max(arr[i], 1 + arr[j])
        return max(arr)