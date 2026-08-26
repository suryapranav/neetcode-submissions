#include <string>
#include <vector>
#include <algorithm>

class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {
        int n = s.length();
        if (n <= 1) return n;

        std::vector<bool> uniqueCheck(256, false);
        int totalUnique = 0;
        for (char c : s) {
            if (!uniqueCheck[c]) {
                uniqueCheck[c] = true;
                totalUnique++;
            }
        }

        std::vector<int> lastIndex(256, -1);
        int maxLength = 0;
        int left = 0;

        for (int right = 0; right < n; ++right) {
            char currentChar = s[right];

            if (lastIndex[currentChar] >= left) {
                left = lastIndex[currentChar] + 1;
            }

            lastIndex[currentChar] = right;
            maxLength = std::max(maxLength, right - left + 1);

            if (maxLength == totalUnique) {
                return maxLength;
            }
        }

        return maxLength;
    }
};
