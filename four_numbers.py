class FourNumbers:
    @staticmethod
    def __get_n_number_sum(nums: [], target: int, n: int, result, results):
        """
        :param nums: Assumes ordered array
        :param target: Target sum
        :param n: Number of entries that add up to :param target:
        :param result: Contains partial result
        :param results: Contains lists of numbers in the array that satisfy the condition (add up to target)
        :return: None
        """
        left, right = 0, len(nums) - 1
        if len(nums) < n or n * nums[0] > target or n * nums[-1] < target:
            return
        if n == 2:
            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    results.append(result + [nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # since array was assumed to be ordered we can check if there are repeated numbers at both the end
                    # or beginning of the array that might satisfy the sum
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                elif s < target:
                    left += 1
                else:  # s < target
                    right -= 1
        else:  # reduce to n == 2
            for i in range(len(nums) - n + 1):
                if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                    FourNumbers.__get_n_number_sum(nums[i + 1:], target - nums[i], n - 1, result + [nums[i]], results)

    @staticmethod
    def get_four_number_sum(target: int, nums: []):
        nums.sort()
        results = []
        FourNumbers.__get_n_number_sum(nums, target, 4, [], results)
        return results
