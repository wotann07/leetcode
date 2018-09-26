class MissingNumber:
    @staticmethod
    def get_missing_int_in_sequence(arr: []):
        """
        This is a linear solution and it will traverse the array entirely
        :param arr: Sequence from 1 to N in an array of size N - 1. ARRAY DOES NOT HAVE TO BE SORTED
        :return: The missing number
        """
        total_sum = sum(arr)
        expected_sum = (len(arr) + 1) * (len(arr) + 2) // 2
        return expected_sum - total_sum

    @staticmethod
    def get_missing_int_in_sorted(arr: []):
        """
        If we assumed the array passed to be sorted then we only have to do half the operations in the worst case
        compared to the previous method
        :param arr: Sequence from 1 to N in an array of size N - 1. Will not work if array not sorted
        :return: The missing number
        """
        i, j = 0, len(arr) - 1
        expected_sum = arr[i] + arr[j]
        while i < j:
            i += 1
            j -= 1
            actual_sum = arr[i] + arr[j]
            if expected_sum > actual_sum:
                return arr[j] + 1
            elif expected_sum < actual_sum:
                return arr[i] - 1

        return 0
