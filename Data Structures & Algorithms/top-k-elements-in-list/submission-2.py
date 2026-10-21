from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # array nums: ints
        # k: int
        # return: the k most frequent elements in the array

        counts = defaultdict(int)

        output = []

        # 1-10^4
        # max 2000 elements

        for value in nums:
            counts[value] = counts[value] + 1

        sorted_counts = sorted(counts, key=counts.get, reverse=True)

        for i in range(k):
            output.append(sorted_counts[i])


        return output