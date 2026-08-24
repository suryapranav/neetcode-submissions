#include <unordered_map>

class Solution {
public:
    bool isAnagram(string s, string t) {
        std::unordered_map<char, int> s_map, t_map;
        if (s.size() != t.size()) { return false; }
        for (int i = 0; i < s.size(); i++) {
            s_map[s[i]]++;
            t_map[t[i]]++;
        }
        return (s_map == t_map);
    }
};
