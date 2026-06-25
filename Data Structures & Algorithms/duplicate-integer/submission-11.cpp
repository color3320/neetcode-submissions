// sorting prac
class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        for(int i = 1; i<nums.size(); ++i){
            if (nums[i] == nums[i-1]){ //Compare the current element with the previous element.
                return true; // if equal true
            }
        }
        return false;
    }
};