# https://leetcode.com/problems/product-of-array-except-self/description/


class ArrayProductExceptSelf:
    @staticmethod
    def product_except_self(nums: [int]):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        size = len(nums)
        prod = 1
        for i in range(size):
            output.append(prod)
            prod *= nums[i]

        prod = 1
        for i in range(size - 1, -1, -1):
            output[i] *= prod
            prod *= nums[i]

        return output
