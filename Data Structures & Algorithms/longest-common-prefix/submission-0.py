class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Consider ["flower", "flow", "flight"]
        prefix = strs[0] # guess the whole first word "flower"
        for i in range(1, len(strs)): # starts with 1 because 1st words is already selected
            word = strs[i] # So it selects next word to compare "flow"
            while prefix != word[0:len(prefix)]:
                # Since flow has 4 letters and "flower" has 6, len(prefix) is 4 for "flow"
                # So it goes does "flower" == "flow" - No
                prefix = prefix[0:len(prefix) - 1]
                # here "flower" becomes "flowe" and loop runs again
                if prefix == "":
                    return ""
        return prefix