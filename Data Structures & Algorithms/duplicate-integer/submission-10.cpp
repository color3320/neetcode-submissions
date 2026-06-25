class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int>seen;
        for (int num : nums){
            if (seen.count(num)){ // same as if num in seen:
                return true;
            } 
            seen.insert(num); 
        }
        return false;    
    }
};