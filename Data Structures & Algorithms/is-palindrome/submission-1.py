class Solution:
    def cleaner(self, s:str) -> str:
        out = []
        for letter in s.lower():
            if ((letter >= 'a' and letter <= 'z') or (letter >= 'A' and letter <= 'Z') or (letter >= '0' and letter <= '9')):
                out.append(letter)
        return "".join(out)
    def isPalindrome(self, s: str) -> bool:
        comparer = self.cleaner(s)
        print(comparer)
        return (comparer[::-1] == comparer)