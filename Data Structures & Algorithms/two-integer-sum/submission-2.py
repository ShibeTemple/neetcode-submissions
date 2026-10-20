class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # list of nums
        # target int

        # return indices i and j
        # where nums[i] + nums[j] == target
        # i =/= j

        # Return the answer with the smaller index first.

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in nums:
                j = nums.index(difference)
                print("i,j",i,j)
                if j == i:
                    continue
                if i < j:
                    return [i,j]
                else:
                    return [j,i]