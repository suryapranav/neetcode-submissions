class Solution:
    def countSubstrings(self, s: str) -> int:
        rows, cols = len(s), len(s)
        count = len(s)
        arr = [[0 for _ in range(rows)] for _ in range(cols)]
        for i in range(0, len(s)):
            for j in range(0, len(s)):
                if i == j: 
                    arr[i][j] = 1
                elif i > j:
                    if (s[i] == s[j]): 
                        arr[i][j] = 2 + arr[i - 1][j + 1]
                        if arr[i][j] == i - j + 1: count += 1
                    else: arr[i][j] = arr[i - 1][j + 1]
        # print(arr)
        return(count)