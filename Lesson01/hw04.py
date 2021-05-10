# Написать программу, которая запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделённых пробелом
# и снова нажать Enter. Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
# ранее сумме и после этого завершить программу.


# user_input = input('Числовой ряд:')


# numbers_list = []
#
# num = ''
# for symbol in user_input:
#     if symbol.isdigit():
#         num = num + symbol
#     else:
#         if num != '':
#             numbers_list.append(input(num))
#             num = ''


def summ_list(s):
    word_list = s.split()
    # print(word_list)
    num_list = [int(num) for num in filter(lambda num: num.isnumeric(), word_list)]
    return sum(num_list)


# def summ_list(list):


s = input('Числовой ряд: ')

print(summ_list(s))
