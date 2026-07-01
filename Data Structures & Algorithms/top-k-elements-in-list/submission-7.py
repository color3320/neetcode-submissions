class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        result = []
        for _ in range(k):
            max_elm = 0
            max_freq = 0
            for elm, freq in count.items():
                if freq>max_freq:
                    max_freq = freq
                    max_elm = elm
            result.append(max_elm)
            del count[max_elm]
        return result    