class Solution:
    # def cleaner(self, s:str) -> str:
    #     out = []
    #     for letter in s.lower():
    #         if ((letter >= 'a' and letter <= 'z') or (letter >= 'A' and letter <= 'Z') or (letter >= '0' and letter <= '9')):
    #             out.append(letter)
    #     return "".join(out)
    # def isPalindrome(self, s: str) -> bool:
    #     comparer = self.cleaner(s)
    #     print(comparer)
    #     return (comparer[::-1] == comparer)

    def isPalindrome(self, s:str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
            print(f"{s[left]} {s[right]}")
        return True