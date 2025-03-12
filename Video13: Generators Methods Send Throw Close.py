from random import randrange

# send 
def f():
    cnt = 0
    for rounds in range(10):
        ret = yield cnt
        if ret is None:
            cnt += 1
        else:
            cnt += 1 + ret

it = f()
for it_val in it:
    print(it_val)
    if randrange(2) == 0:
        val = it.send(100)
        print(val)

# close
def g():
    i = 1
    while True:
        yield i
        i += 2

gi = g()
for i in gi:
    print(i)
    if i == 101:
        gi.close()


# throw method
def k():
    i = 1
    while True:
        yield i
        i += 2


ki = k()
for i in ki:
    print(i)
    if i == 101:
        ki.throw(Exception)
