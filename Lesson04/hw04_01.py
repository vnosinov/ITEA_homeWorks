# Реализовать функцию, которая на вход принимает целое положительное число n и возвращает при вызове
# объект-генератор, который по запросу будет возвращать значение факториала всех чисел от 0 до n.
#  n! = n * (n-1) * (n-2) * (n-3) * (n-4) * .......


def factorial_gen(n):
    i = 1
    for j in range(1, n + 1):
        i *= j
        yield i


def factorial(n):
    f = 1
    for i in range(1 ,n+1):
        f *= i
    return f


print(next(factorial_gen(3)))

print(factorial(3))
