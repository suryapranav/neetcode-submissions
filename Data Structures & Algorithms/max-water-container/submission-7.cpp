class Solution {
public:
    int maxArea(vector<int>& heights) {
        int l = 0;
        int r = heights.size() - 1;
        int area = std::numeric_limits<int>::lowest();
        int area_current = 0;

        while (l < r) {
            area_current = std::min(heights[l], heights[r]) * (r - l);
            if (area_current > area) {
                area = area_current;
            }
            if (heights[l] >= heights[r]) {
                r--;
            } else {
                l++;
            }
        }
        return area;
    }
};
