#!/usr/bin/python

from deadsimplethreading import threaded, run_threaded

if __name__ == '__main__':
    import time

    def example():
        def exfunc(i, foo):
            time.sleep(5)
            #print(i, foo)
            return i * i

        for i in range(100):
            yield threaded(exfunc, i, foo='bar')

    res = list(run_threaded(example()))
    print(res)
