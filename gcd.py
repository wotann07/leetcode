class GCD:

    @staticmethod
    def __find_gcd(a, b):
        return b if a == 0 else GCD.__find_gcd(b % a, a)

    @staticmethod
    def __find_gcd_alt(a, b):
        while b:
            a, b = b, b % a
        return a

    # TODO: Write tests
    @staticmethod
    def generalized_gcd(arr):
        # using Euclidean algorithm
        gcd = arr[0]
        for n in arr:
            gcd = GCD.__find_gcd(n, gcd)

        return gcd
