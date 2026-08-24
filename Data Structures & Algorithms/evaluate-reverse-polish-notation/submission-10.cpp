class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        std::stack<int> st;

        for(std::string& token : tokens) {
            if (token == "+" || token == "-" || token == "/" || token == "*") {
                if (st.size() < 2) {
                    throw std::invalid_argument("Invalid RPN expression");
                }

                int rhs = st.top();
                st.pop();
                int lhs = st.top();
                st.pop();

                if (token == "+") st.push(lhs + rhs);
                else if (token == "-") st.push(lhs - rhs);
                else if (token == "*") st.push(lhs * rhs);
                else if (token == "/") {
                    if (rhs == 0) {
                        throw std::runtime_error("Dividing by zero");
                    }
                    st.push(lhs / rhs);
                }
            } else {
                st.push(std::stoi(token));
            }
        }
        if (st.size() != 1) {
            throw std::invalid_argument("Invalid RPN expression.");
        }
        return st.top();
    }
};
