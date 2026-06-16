class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        std::unordered_map<int, int>count;
        for(int num : nums){
            count[num]++;
        }
        std::priority_queue<std::pair<int, int>,
        std::vector<std::pair<int,int>>,
        std::greater<std::pair<int,int>>>minHeap;

        for (auto& [num, freq] : count){
            minHeap.push({freq,num});
            if(minHeap.size()>k){
                minHeap.pop();
            }
        }
        vector<int>res;
        for (int i = 0; i < k; i++){
            res.push_back(minHeap.top().second);
            minHeap.pop();
        }
        return res;
    }
};
