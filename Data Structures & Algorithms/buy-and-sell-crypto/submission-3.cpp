class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int min_left = std::numeric_limits<int>::max();
        int max_profit = 0;

        for(const auto& element : prices) {
            if (element < min_left) {
                min_left = element;
            }
            else if (element - min_left > max_profit){
                max_profit = element - min_left;
            }
        }
        return max_profit;
    }
};
