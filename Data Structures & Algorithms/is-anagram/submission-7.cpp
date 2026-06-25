// Removing char 1 by 1 and comparing
// class Solution {
// public:
//     bool isAnagram(string s, string t) {
//         if (s.size() != t.size()){
//             return false;
//         }
//         for (char c:s){
//             size_t pos = t.find(c);
//             if(pos == string::npos) {
//                 return false;
//             }
//             t.erase(pos, 1);
//         }
//         return true;
//     }
// };

// sorting
// class Solution {
// public:
//     bool isAnagram(string s, string t){
//         if (s.size()!=t.size()){
//             return false;
//         }
//         sort(s.begin(), s.end());
//         sort(t.begin(), t.end());
//         return s == t;
//     }
// };
// hash map
// class Solution {
// public:
//     bool isAnagram(string s, string t){
//         if(s.size() != t.size()){
//             return false;
//         }
//         unordered_map<char, int>countS;
//         unordered_map<char,int>countT;
//         for (int i = 0; i<s.size(); ++i){
//             countS[s[i]]++;
//             countT[t[i]]++;
//         }
//         return countS == countT;
//     }
// };
// hash table
class Solution {
public:
    bool isAnagram(string s, string t){
        if (s.size()!= t.size()){
            return false;
        }
        vector<int> count(26,0);
        for (int i = 0; i<s.size(); ++i){
            count[s[i] - 'a']++;
            count[t[i] - 'a']--;
        }
        for (int val : count) {
            if (val !=0){
                return false;
            }
        }
        return true;
    }
};


