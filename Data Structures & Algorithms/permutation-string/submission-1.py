from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if k > len(s2):
            return False

        s1_count = Counter(s1)
        s2_count = Counter(s2[:k])

        if s1_count == s2_count:
            return True

        for i in range(k, len(s2)):
            s2_count[s2[i]] += 1
            
            left_char = s2[i - k]
            s2_count[left_char] -= 1
            if s2_count[left_char] == 0:
                del s2_count[left_char]

            if s1_count == s2_count:
                return True

        return False