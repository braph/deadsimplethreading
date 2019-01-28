#!/usr/bin/python3

import queue
import threading

def threaded(func, *args, **kwargs):
    return (func, args, kwargs)

def run_threaded(iterator, parallel=-1):
    threads = queue.Queue(parallel)
    results = queue.Queue()

    def start_threaded(func, args, kwargs):
        try:
            results.put(func(*args, **kwargs))
        finally:
            threads.get()

    def start_iterator(iterator):
        for threaded in iterator:
            thr = threading.Thread(target=start_threaded, args=threaded)
            threads.put(thr)
            thr.start()

    bg_thr = threading.Thread(target=start_iterator, args=(iterator,))
    bg_thr.start()

    while True:
        try:   yield results.get(True, 1)
        except GeneratorExit: return
        except queue.Empty:   pass

        if (not bg_thr.is_alive() and
                threads.qsize() == 0 and
                results.qsize() == 0):
            break

    while True:
        try:   yield results.get_nowait()
        except GeneratorExit: return
        except queue.Empty:   break

