class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # array: nums
        # contains: ints
        # return true: if duplicate
        # return false otherwise

        # length >= 0
        # legnth <= 10^5
        # nums can be negative or positive

        # can be any number of duplicates btw... more than 2 is possible

        converted_set = set(nums)
        if (len(converted_set) != len(nums)):
            return True
        return False