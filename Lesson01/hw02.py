# Формула для расчета числа Фибоначчи
# F(n) = F(n-1) + F(n-2)
# F1 = 1, F2 = 1
# 1, 1, 2,

# с использованием цикла
def fibo(n):
    f1 = 1
    f2 = 1
    i = 0
    while i < n - 2:
        f_temp = f1 + f2
        f1 = f2
        f2 = f_temp
        i += 1
    return f2


# c рекурсией
def recursion_fibo(n):
    if n in (1, 2):
        return 1
    return recursion_fibo(n - 1) + recursion_fibo(n - 2)


number = int(input('Введите номер позиции числа Фибоначчи N : '))
print(f'Получение числа Фибоначчи циклом {fibo(number)}')
print(f'Получение числа Фибоначчи рекурсией {recursion_fibo(number)}')
