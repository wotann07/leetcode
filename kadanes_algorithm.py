class Kadane:
    @staticmethod
    def get_max_contiguous_sum(arr: []):
        """
        :type arr: [] contains positive and negative integers
        :rtype: int maximum contiguous sum
        """

        max_sum = curr_max = arr[0]
        for i in range(1, len(arr)):
            curr_max = max(arr[i], arr[i] + curr_max)
            max_sum = max(curr_max, max_sum)

        return max_sum
