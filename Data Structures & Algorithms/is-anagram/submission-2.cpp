#include <string>
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()){
            return false;
        }
        for (char c:s){
            size_t pos = t.find(c);
            if(pos == string::npos) {
                return false;
            }
            t.erase(pos, 1);
        }
        return true;
    }
};
