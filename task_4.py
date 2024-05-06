def mul_table(number):

    for i in range(0, number + 1):

        f_string_1 = f'{i}'
        if i == 0:
            f_string_1 = f_string_1.replace('0', ' ')

        print(f_string_1, end='')

        for j in range(1, number + 1):
            f_string_2 = '{:>3}'.format(j*i)
            if i == 0:
                f_string_2 = '{:>3}'.format(j)

            print(f_string_2, end='')
        print('')


if __name__ == '__main__':
    mul_table(5)