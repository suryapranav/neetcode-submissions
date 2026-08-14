class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        volume_final = 0
        while left < right:
            volume = min(heights[left], heights[right]) * (right - left)
            if volume > volume_final: 
                volume_final = volume
            if heights[left] < heights[right]:
                left += 1
                continue
            if heights[right] <= heights[left]:
                right -= 1
                continue
        return volume_final