from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)  # frequency map: number -> count
        return [item for item, _ in heapq.nlargest(k, count.items(), key=lambda x: x[1])]
