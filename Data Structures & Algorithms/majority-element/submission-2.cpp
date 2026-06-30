class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i<n; ++i){
            int c = 0;
            for (int j = 0; j<n; ++j){
                if (nums[j] == nums[i]){
                    c += 1;
                }
            }
            if (c > n/2){
                return nums[i];
            }
        }
        return -1;
    }
};