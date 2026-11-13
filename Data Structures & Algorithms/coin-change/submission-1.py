class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [0] + [float('inf')] * (amount)
        count_max, count = 0, 0
        for i in range(0, amount + 1):
            for elem in (coins):
                if i - elem >= 0:
                    arr[i] = min(arr[i], 1 + arr[i-elem])
        if arr[amount] == float('inf'): return -1
        else: return arr[amount]