class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        std::vector<int> s1_counter(256, 0);
        int unique = 0;
        for (unsigned char c : s1) {
            if (s1_counter[c] == 0) {
                s1_counter[c]++;
                unique++;
            } else {
                s1_counter[c]++;
            }
        }
        int window_size = s1.size();
        int left = 0;
        int right = s1.size() - 1;
        while (right < s2.size()) {
            std::vector<int> s2_counter(256, 0);
            for (int i = left; i <= right; i++) {
                s2_counter[s2[i]]++;
            }
            if (s2_counter == s1_counter) {
                return true;
            } else {
                left++;
                right++;
            }
        }
        return false;
    }
};
