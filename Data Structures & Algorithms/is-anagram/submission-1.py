class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_map, t_map = {}, {}
        for letter1 in s:
            s_map[letter1] = s_map.get(letter1, 0) + 1
        for letter2 in t:
            t_map[letter2] = t_map.get(letter2, 0) + 1
        return s_map == t_map
            
        