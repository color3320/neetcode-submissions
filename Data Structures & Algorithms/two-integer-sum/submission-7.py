# prac
# add each one by one till target brute
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return []

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i in range(len(nums)):
            num = nums[i]
            A.append([num,i])
        A.sort()
        i,j = 0, len(nums)-1
        while i<j:
            sums = A[i][0] + A[j][0]
            if sums==target:
                return[min(A[i][1],A[j][1]), max(A[i][1],A[j][1])]
            elif sums<target:
                i += 1
            else:
                j -= 1
        return []

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]: