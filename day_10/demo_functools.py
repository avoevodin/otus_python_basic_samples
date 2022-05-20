from functools import lru_cache, wraps, partial


def cache_fib(func):
    cache = {}

    @wraps(func )
    def wrapper(n):
        if n in cache:
            return cache[n]
        res = func(n)
        cache[n] = res
        return res
    return wrapper


# @cache_fib
@lru_cache
def fib(n):
    """
    Calculates fib
    :param n:
    :return:
    """
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


def demo_fib():
    print(fib)
    print(fib.__name__)
    print(fib.__doc__)
    print([fib(i) for i in range(20)])


def demo_partials():
    def square(n):
        return n ** 2

    print(pow(2, 3))
    pow3 = partial(pow, exp=3)
    print(pow3(3))
    print(pow3(4))


def main():
    demo_fib()
    demo_partials()


if __name__ == '__main__':
    main()
