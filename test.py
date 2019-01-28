#!/usr/bin/python

import time
from deadsimplethreading import threaded, run_threaded, threaded_func

def example():
    def exfunc(i, foo):
        time.sleep(1)
        return i * i

    for i in range(100):
        yield threaded(exfunc, i, foo='bar')

print('example():', list(run_threaded(example())))

@threaded_func
def example2(my_arg):
    print('my_arg:', my_arg)

    def exfunc(i, foo):
        time.sleep(1)
        return i * i

    for i in range(100):
        yield threaded(exfunc, i, foo='bar')

print('example2("an_arg"):', list(example2("an_arg")))

print('example2("an_arg", parallel=20):', list(example2("an_arg", parallel=20)))
