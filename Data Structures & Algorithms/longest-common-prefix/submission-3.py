# Sorting
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort() # list is sorted now
        # grabbing extremes
        first = strs[0]
        last = strs[len(strs) - 1]
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            # Since our list is sorted the last word and first word are
            # the one which will have the least matches 
            # this loop will keep going through each letter till there is mismatch
            i += 1
        return first[0:i]

        