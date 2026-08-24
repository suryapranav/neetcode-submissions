#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> hash;
        int complement = 0;
        for(int i = 0; i < nums.size(); i++) {
            complement = target - nums[i];
            if (hash.find(complement) != hash.end()) {
                return {hash[complement], i};
            } else {
                hash[nums[i]] = i;
            }
        }
    }
};
