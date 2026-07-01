// brute force
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        std::string prefix = strs[0];
        int n = strs.size(); // we write this in c++ and not in python because
                            // in python it is only calculated once but in c++ it'll be calculated everytime
        for (int i = 1; i < n; i++){
            std::string word = strs[i];
            while (prefix != word.substr(0, prefix.length())){
                prefix = prefix.substr(0, prefix.length() - 1);
                if (prefix == ""){
                    return "";
                }
            }
        }
        return prefix;

    }
};