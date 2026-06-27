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
        # consider nums = [7, 4, 6, 1, 11, 8] and target = 10
        A = []
        # for i in range(len(nums)):
        #     num = nums[i]
        #     A.append([num,i])
        # Gives output - A = [[7, 0], [4, 1], [6, 2], [1, 3], [11, 4], [8, 5]]
        
        for i, num in enumerate(nums):
            A.append([num, i])
        # Gives output - A = [[7, 0], [4, 1], [6, 2], [1, 3], [11, 4], [8, 5]] 

        A.sort()
        # Gives output - A = [[1, 3], [4, 1], [6, 2], [7, 0], [8, 5], [11, 4]]

        i,j = 0, len(nums)-1 # Two pointer setup
        while i<j:
            sums = A[i][0] + A[j][0]
            # For first loop - A[0][0] = [1,3] and A[5][0] = [11,4]
            # (since j = len(nums)-1)
            
            if sums==target:
                return[min(A[i][1],A[j][1]), max(A[i][1],A[j][1])]
            elif sums<target:
                i += 1
            else:
                j -= 1
        return []

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]: