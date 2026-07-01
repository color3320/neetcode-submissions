# # Hashmap - sorting - converting to list
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         temp = defaultdict(list)
#         for s in strs:
#             sortedS = ''.join(sorted(s))
#             temp[sortedS].append(s)
#         return list(temp.values())

# Hash table and char count    
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
            temp[tuple(count)].append(s)
        return list(temp.values())
