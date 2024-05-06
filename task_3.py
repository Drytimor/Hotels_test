def prime_number(min_num, max_num):

    if min_num == 2:
        result = [2]
    else:
        result = []

    if min_num % 2 == 0:
        min_num += 1

    if max_num % 2 != 0:
        max_num += 1

    for i in range(min_num, max_num, 2):
        for j in range(3, i-1, 2):
            if i % j == 0:
                break
        else:
            result.append(i)

    return result


if __name__ == '__main__':
    print(prime_number(11, 20))