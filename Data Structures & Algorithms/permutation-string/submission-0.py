class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = {}
        for letter in s1:
            s1_count[letter] = s1_count.get(letter, 0) + 1

        start = 0
        end = len(s1)

        while end <= len(s2):
            s2_count = {}
            
            for i in range(start, end):
                letter = s2[i]
                s2_count[letter] = s2_count.get(letter, 0) + 1
            
            if s1_count == s2_count:
                return True
            
            start += 1
            end += 1

        return False