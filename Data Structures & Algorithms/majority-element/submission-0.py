class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res = maxcount = 0
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if maxcount < count[num]:
                res = num
                maxcount = count[num]
        return res

        