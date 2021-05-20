# Написать программу, которая запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделённых пробелом
# и снова нажать Enter. Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной
# ранее сумме и после этого завершить программу.


# all_sum = 0
#
# EXIT = True
# print('Введите числовой ряд, символ для выхода"#"')
# while True:
#     s = input('Числовой ряд: ')
#
#
#     def sum_list(s):
#         global EXIT
#         word_list = s.split()
#         if "#" in word_list:
#             EXIT = False
#         num_list = [int(num) for num in filter(lambda num: num.isnumeric(), word_list)]
#         return sum(num_list)
#
#     all_sum += sum_list(s)
#     print(all_sum)

all_sum = 0
print('Введите числовой ряд, символ для выхода"#"')
while True:
    s = input('Числовой ряд: ')
    word_list = s.split()
    # if "#" in word_list:
    #     print('')

    num_list = [int(num) for num in filter(lambda num: num.isnumeric(), word_list)]

    all_sum += sum(num_list)
    print(all_sum)
    if "#" in word_list:
        break
