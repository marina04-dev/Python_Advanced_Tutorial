# decorators with arguments
def lines_below(n):
    def line_below(func):
        def line(*args):
            func(*args)
            for _ in range(n):
                for i in range(n):
                    for arg in args:
                        print(arg, end="")
                print()
        return line
    return line_below


@lines_below(n=4)
def my_print(m, *args):
    print("test")

my_print(5, "*", "-", "*")


# variables with state in decorators
from math import sqrt

def valid_int_gt_zero(func):
    def decorated(val):
        if not isinstance(val, int):
            raise TypeError("Not An Integer")
        elif val < 0:
            raise ValueError("Negative Value")
        else:
            decorated.calls += 1
            return func(val)
    decorated.calls = 0
    return decorated

@valid_int_gt_zero
def int_sqrt(val):
    return int(sqrt(val))

print(int_sqrt(2))
print(int_sqrt(4))
print("Calls: " + str(int_sqrt.calls))
