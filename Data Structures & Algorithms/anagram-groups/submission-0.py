class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pairs = sorted([(''.join(sorted(s)), s) for s in strs], key=lambda x: x[0])
        return [[word for _, word in group] for key, group in groupby(pairs, key=lambda x: x[0])]
