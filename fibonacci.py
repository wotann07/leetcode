class Fibonacci:
    @staticmethod
    def _get_fibonacci_helper(n: int, fib_computed: {}):
        fib_computed[0] = 0
        fib_computed[1] = 1
        if n <= 1:
            return fib_computed[n]

        if not fib_computed.get(n):
            fib_computed[n] = Fibonacci._get_fibonacci_helper(n - 1, fib_computed) + Fibonacci._get_fibonacci_helper(
                n - 2, fib_computed)

        return fib_computed[n]

    @staticmethod
    def get_fibonacci(n: int):
        return Fibonacci._get_fibonacci_helper(n, {})
