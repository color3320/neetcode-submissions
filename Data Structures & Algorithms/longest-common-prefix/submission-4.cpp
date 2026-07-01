// sorting
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        std::sort(strs.begin(), strs.end());
        std::string first = strs[0];
        std::string last = strs[strs.size() - 1];
        int i = 0;
        int limit = std::min(first.length(), last.length());
        while (i < limit && first[i] == last[i]){
            i += 1;
        }
        // C++ creates a limit variable. If one word is 4 letters and the other is 6, 
        // we can't check past the 4th letter, or the program will crash. Python handles 
        // this safety check directly inside the while loop
        return first.substr(0, i);
    }
};