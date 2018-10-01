class ReplaceWithGreatest:
    @staticmethod
    def replace_with_greatest(arr: []):
        """
        Replace all of the elements in arr with the greatest to the right
        :param arr: Arr to modify
        """

        tmp = arr[:len(arr) - 1]
        curr_max = arr[-1]
        arr[-1] = -1
        for i in range(len(tmp) - 1, -1, -1):
            arr[i] = curr_max
            if tmp[i] > curr_max:
                curr_max = tmp[i]
