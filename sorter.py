class Sorter:
    @staticmethod
    def merge_sort_helper(arr: []):
        if len(arr) == 1:
            return arr
        else:
            middle = len(arr) // 2
            left_arr = arr[:middle]
            right_arr = arr[middle:]

            Sorter.merge_sort_helper(left_arr)
            Sorter.merge_sort_helper(right_arr)

            Sorter.merge(arr, left_arr, right_arr)

    @staticmethod
    def merge(arr: [], left: [], right: []):
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        for i in range(i, len(left)):
            arr[k] = left[i]
            k += 1

        for j in range(j, len(right)):
            arr[k] = right[j]
            k += 1

    @staticmethod
    def merge_sort(arr: []):
        Sorter.merge_sort_helper(arr)
        return arr

    @staticmethod
    def bubble_sort(arr: []):
        not_sorted = True
        while not_sorted:
            not_sorted = False
            for i in range(len(arr) - 1):
                if arr[i + 1] < arr[i]:
                    tmp = arr[i]
                    arr[i] = arr[i + 1]
                    arr[i + 1] = tmp
                    not_sorted = True

        return arr

    @staticmethod
    def heap_sort():
        pass

    @staticmethod
    def selection_sort(arr: []):
        for i in range(len(arr)):
            pos_min = i
            for j in range(i, len(arr)):
                if arr[j] < arr[pos_min]:
                    pos_min = j
            tmp = arr[i]
            arr[i] = arr[pos_min]
            arr[pos_min] = tmp

        return arr

    @staticmethod
    def insertion_sort():
        pass

    @staticmethod
    def shell_sort():
        pass

    @staticmethod
    def quick_sort():
        pass
