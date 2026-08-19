class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        frequency = {}
        n = 0
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, value in frequency.items():
            buckets[value].append(key)
        # print(buckets)
        buckets_flat = [item for sublist in buckets for item in sublist]
        # print(buckets_flat)
        return buckets_flat[-k:]