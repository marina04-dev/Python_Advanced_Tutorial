def decorate_with_lines(func):
    def dec():
        print("=" * 20)
        func()
        print("=" * 20)
    return dec

def decorate_with_stars(func):
    def dec():
        print("*" * 20)
        func()
        print("*" * 20)
    return dec

@decorate_with_stars
@decorate_with_lines
def some_func():
    print("Hello World!")

some_func()
