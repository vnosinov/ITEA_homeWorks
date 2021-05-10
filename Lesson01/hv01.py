# Написать декоратор, который будет печатать на экран время работы функции.
import time


def time_of_fun(f):
    def wrapped(*args):
        start_time = time.time()
        res = f(*args)
        print("{:100.98f}".format(time.time() - start_time))
        return res
    return wrapped


@time_of_fun
def func(n):
    if n in (1, 2):
        return 1
    return func(n - 1) + func((n - 2))


print(func(10))
