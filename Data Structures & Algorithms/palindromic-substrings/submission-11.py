class Solution:
    # solution 1: calculate maximum length of palindromic substring within a start and end, if the substring itself is a palindrome, count it.
    ''' def countSubstrings(self, s: str) -> int:
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
        return(count) '''

    # solution 2: 2 pointers at every location in the array, and they move in opposite directions. Repeat with pointers separated to get even length palindromes.
    def countSubstrings(self, s:str) -> int:
        length, count = len(s), 0
        for i in range(0, length):
            left, right = i , i
            while left >= 0 and right < length:
                if s[left] == s[right]: 
                    count += 1
                    left -= 1
                    right += 1
                else: break # break immediately if non-palindrome is detected
            left, right = i, i + 1
            while left >= 0 and right < length:
                if s[left] == s[right]: 
                    count += 1
                    left -= 1
                    right += 1
                else: break
        return count
