import time

def timeit(func):
    def decorator(*args, **kwargs):
        t0 = time.time()
        ret = func(*args, **kwargs)
        t1 = time.time()
        print("Total Time: " + str(t1-t0))
        return ret
    return decorator

def memoize(func):
    def decorator(arg):
        results_memory = {}
        if arg in results_memory:
            return results_memory[arg]
        else:
            return func(arg)
    return decorator



@timeit
def fib(n):
    @memoize
    def recursive(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return recursive(n-1) + recursive(n-2)
    print(f"Fib({n})={recursive(n)}")
