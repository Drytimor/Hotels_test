def declension(number):

    ending = 'ов'

    if number % 10 == 1 and number % 100 // 10 != 1:
        ending = ''
    elif number % 10 in (2, 3, 4):
        ending = 'а'

    return f'{number} компьютер{ending}'


if __name__ == '__main__':
    print(declension(1048))
