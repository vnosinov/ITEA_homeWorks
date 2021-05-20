# Реализовать функцию, которая принимает три позиционных
# аргумента и возвращает сумму наибольших двух из них.

def selecting_sum(a, b, c):

    if a == b or a == c or b == c:
        print(f'Условия не соответствуют задаче суммируем три аргумента')
        return a + b + c
    else:
        if a < b and a < c:
            return b + c
        elif b < a and b < c:
            return a + c
        return a + b


print(selecting_sum(6, 1, 5))


def sel_sum2(a, b, c):
    my_list = [a, b, c]
    return sum(my_list) - min(my_list)


print(sel_sum2(6, 1, 5))