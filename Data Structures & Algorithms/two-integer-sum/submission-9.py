# prac
# add each one by one till target brute
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return []

# class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
        # consider nums = [7, 4, 6, 1, 11, 8] and target = 10
        # A = []
        # for i in range(len(nums)):
        #     num = nums[i]
        #     A.append([num,i])
        # Gives output - A = [[7, 0], [4, 1], [6, 2], [1, 3], [11, 4], [8, 5]]
        
        # for i, num in enumerate(nums):
        #     A.append([num, i])
        # Gives output - A = [[7, 0], [4, 1], [6, 2], [1, 3], [11, 4], [8, 5]] 

        # A.sort()
        # Gives output - A = [[1, 3], [4, 1], [6, 2], [7, 0], [8, 5], [11, 4]]

        # i,j = 0, len(nums)-1 # Two pointer setup
        # while i<j:
        #     sums = A[i][0] + A[j][0]

            
        #     if sums==target:
        #         return[min(A[i][1],A[j][1]), max(A[i][1],A[j][1])]
        #     elif sums<target:
        #         i += 1
        #     else:
        #         j -= 1
        # return []

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # consider nums = [7, 4, 6, 1, 11, 8] and target = 10
        seen = {} # seen =  {number : index}
        for i, j in enumerate(nums):
            # Iteration 1 : i = 0 (index), j = 7 (value)
            complement = target - j
            # calculate complement 10 - 7 = 3
            if complement in seen:
                # 3 not in seen then
                return[seen[complement], i]
                # if in dictionary for eg 4 return 
                # seen[complement] means "look up the index of the number 4 in the dictionary". 
                # The dictionary tells us it is at index 1.
                # and i already present there is index for current number 
            seen[j] = i
            # if not in dictionary
            # add current number and it's index to dictionary (seen)