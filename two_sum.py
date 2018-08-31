# https://leetcode.com/problems/two-sum/description/


class TwoSum:
    @staticmethod
    def two_sum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d_nums = {}
        for i in range(len(nums)):
            if target - nums[i] in d_nums.keys() and d_nums[target - nums[i]] != i:
                return [d_nums[target - nums[i]], i]
            d_nums[nums[i]] = i
