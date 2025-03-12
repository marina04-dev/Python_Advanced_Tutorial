def decorate_gt_zero(func):
    def dec(a,b):
        if a<=0 and b<=0:
            print("Error: Both Arguments must Be Positive!")
        else:
            func(a,b)
    return dec

@decorate_gt_zero
def some_func(a,b):
    print(a*b)

some_func(1,3)
some_func(0, 5)


def decorate_with_lines(func):
    def dec(*args,**kwargs):
        print("=" * 20)
        func(*args, **kwargs)
        print("=" * 20)
    return dec

@decorate_with_lines
def some_calc(a,b):
    print(a*b)

some_calc(3,6)


def decorate_gt_zero_int(func):
    def dec(*args):
        for i in args:
            if i > 0 and isinstance(i, int):
                return func(*args)
            else:
                print("Error: All Numbers Must Be Integers Under Zero!")
                return None
    return dec

@decorate_gt_zero_int
def product(*args):
    prod = 1
    for i in args:
        prod *= i
    return prod

print(product(3,4,5,6,7,8,9,2))
