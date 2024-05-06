def common_divisor(array):
    min_num = min(array)
    result = []

    i = 2
    while i <= min_num**0.5:
        if min_num % i == 0:
            result.append(i)
            if i != min_num//i:
                result.append(min_num // i)
        i += 1

    result.append(min_num)

    for num in array:
        i = 0
        l = len(result)
        while i < l:
            if num % result[i] != 0:
                del result[i]
                l -= 1
                i -= 1
            i += 1

    return sorted(result)


if __name__ == '__main__':
    print(common_divisor([12, 42, 18]))


