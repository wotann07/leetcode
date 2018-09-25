class Kadane:
    @staticmethod
    def get_max_contiguous_sum_subarray(arr: []):
        """
        :param arr: Contains positive and negative integers
        :return: Subarray containing the maximum contiguous sum
        """

        start_pos = end_pos = marker = 0
        max_sum = curr_max = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > arr[i] + curr_max:
                curr_max = arr[i]
                marker = i
            else:
                curr_max = arr[i] + curr_max

            if curr_max > max_sum:
                max_sum = curr_max
                end_pos = i
                start_pos = marker

        return arr[start_pos:end_pos + 1]

    @staticmethod
    def get_max_contiguous_sum(arr: []):
        """
        :type arr: [] Contains positive and negative integers
        :rtype: int The maximum contiguous sum
        """
        return sum(Kadane.get_max_contiguous_sum_subarray(arr))
