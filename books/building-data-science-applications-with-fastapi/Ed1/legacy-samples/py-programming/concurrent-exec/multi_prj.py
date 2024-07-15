# from multiprocessing import Pool, Process
import multiprocessing as mp
from multiprocessing import (
    Process, Pipe, Lock,
    Value, Array, Manager,
    Pool, TimeoutError
)
import time
import os

'''
# def f(x):
#     return x*x

# def f(name):
#     print('hello', name)


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def f(name):
    info('function f')
    print('hello', name)


if __name__ == '__main__':
    # with Pool(5) as p:
    #     print(p.map(f, [1, 2, 3]))

    # p = Process(target=f, args=('bob',))
    # p.start()
    # p.join()

    info('main line')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()
'''

#  set_start_method() ----------------------------------

# def foo(q):
#     q.put('hello')


# if __name__ == '__main__':
#     # behind spawn / fork / forkserver
#     mp.set_start_method('spawn')

#     q = mp.Queue()

#     p = mp.Process(target=foo, args=(q,))

#     p.start()
#     print(q.get())
#     p.join()


# get_context() ----------------------------------

# def foo(q):
#     q.put('hello')


# if __name__ == '__main__':
#     # ctx abbrev. to context
#     ctx = mp.get_context('spawn')

#     q = ctx.Queue()
#     p = ctx.Process(target=foo, args=(q,))
#     p.start()
#     print(q.get())
#     p.join()


# communication channel between processes ----------------------------------
# Queues examples --------------

# def f(q):
#     q.put([42, None, 'hello'])


# if __name__ == '__main__':
#     q = Queue()

#     p = Process(target=f, args=(q,))

#     p.start()
#     print(q.get())    # prints "[42, None, 'hello']"
#     p.join()


# Pipes examples --------------
# def f(conn):
#     conn.send([42, None, 'hello'])
#     conn.close()


# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe()

#     p = Process(target=f, args=(child_conn,))
#     p.start()
#     print(parent_conn.recv())   # prints "[42, None, 'hello']"
#     p.join()


# Synchronization  ----------------------------------
# def f(l, i):
#     # l mean lock, i mean values
#     l.acquire()
#     try:
#         print('hello world', i)
#     finally:
#         l.release()


# if __name__ == '__main__':
#     lock = Lock()

#     for num in range(10):
#         # this Process using frequently
#         Process(target=f, args=(lock, num)).start()


# Sharing state  ----------------------------------
# def f(n, a):
#     n.value = 3.1415927
#     for i in range(len(a)):
#         a[i] = -a[i]


# if __name__ == '__main__':
#     # Shared memory
#     num = Value('d', 0.0)
#     arr = Array('i', range(10))

#     p = Process(target=f, args=(num, arr))
#     p.start()
#     p.join()

#     print(num.value)
#     print(arr[:])


# def f(d, l):
#     d[1] = '1'
#     d['2'] = 2
#     d[0.25] = None
#     l.reverse()


# if __name__ == '__main__':
#     # Server process
#     with Manager() as manager:
#         d = manager.dict()
#         l = manager.list(range(10))

#         p = Process(target=f, args=(d, l))
#         p.start()
#         p.join()

#         print(d)
#         print(l)


# workers pool ----------------------------------
def f(x):
    return x*x


if __name__ == '__main__':
    # start 4 worker processes
    with Pool(processes=4) as pool:

        # print "[0, 1, 4,..., 81]"
        print(pool.map(f, range(10)))

        # print same numbers in arbitrary order
        for i in pool.imap_unordered(f, range(10)):
            print(i)

        # evaluate "f(20)" asynchronously
        res = pool.apply_async(f, (20,))      # runs in *only* one process
        print(res.get(timeout=1))             # prints "400"

        # evaluate "os.getpid()" asynchronously
        res = pool.apply_async(os.getpid, ())  # runs in *only* one process
        print(res.get(timeout=1))             # prints the PID of that process

        # launching multiple evaluations asynchronously *may* use more processes
        multiple_results = [pool.apply_async(os.getpid, ()) for i in range(4)]
        print([res.get(timeout=1) for res in multiple_results])

        # make a single worker sleep for 10 secs
        res = pool.apply_async(time.sleep, (10,))
        try:
            print(res.get(timeout=1))
        except TimeoutError:
            print("We lacked patience and got a multiprocessing.TimeoutError")

        print("For the moment, the pool remains available for more work")

    # exiting the 'with'-block has stopped the pool
    print("Now the pool is closed and no longer available")
