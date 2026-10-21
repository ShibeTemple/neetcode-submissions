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

        #print(counts)
        sorted_counts = sorted(counts, key=counts.get, reverse=True)
        #print(sorted_counts)

        for i in range(k):
            output.append(sorted_counts[i])

        #print(output)

        return output