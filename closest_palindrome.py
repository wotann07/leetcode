class ClosestPalindrome:
    @staticmethod
    def __get_palindrome(n: str):
        if len(n) == 1:
            return n
        else:
            return int(n[:(len(n) + 1) // 2] + n[(len(n) + 1) // 2 - (1 + len(n) % 2)::-1])

    @staticmethod
    def get_closest_palindrome(n: int):
        if n == 10:
            return 9

        j = ClosestPalindrome.__get_palindrome(str(n))
        f = len(str(n)) // 2
        i = ClosestPalindrome.__get_palindrome(str((n // (10 ** f) - 1) * (10 ** f)))
        k = ClosestPalindrome.__get_palindrome(str((n // (10 ** f) + 1) * (10 ** f)))

        # returning smaller of two palindromes is ensured by the order of i, j, k
        return min(i, j, k, key=lambda x: abs(n - x))
