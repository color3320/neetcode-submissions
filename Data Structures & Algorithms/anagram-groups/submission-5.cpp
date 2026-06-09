class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;
        for (string s : strs){
            int count[26] = {0};
            for(char c : s){
                count[c - 'a']++;
            }
            string key;                             // extra in 
            for (int i = 0; i<26; i++){             // c++
                key += '#' + to_string(count[i]);   // compared to python
            }
            groups[key].push_back(s);
        }
        vector<vector<string>> result;
        for (auto& [k, group] : groups) {
            result.push_back(group);
        }
        return result;
    }
};
