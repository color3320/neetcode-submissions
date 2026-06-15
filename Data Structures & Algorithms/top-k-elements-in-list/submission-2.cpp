class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int>count;
        for (int num: nums){
            count[num]++;
        }
        std:vector<int>result;
        for (int i = 0; i<k; i++){
            int maxElm = 0;
            int maxFreq = 0;
            for (auto&[elm, freq]:count){
                if (freq>maxFreq){
                    maxFreq = freq;
                    maxElm = elm;
                }
            }
            result.push_back(maxElm);
            count.erase(maxElm);
        }
        return result;
    }
};
