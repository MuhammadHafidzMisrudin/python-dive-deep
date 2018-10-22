def factors_number(num):
    factors_container = []

    # loop through.
    for curr_num in range(1, num + 1):
        print('curr_num', curr_num)

        # check the factors of a number.
        if (num % curr_num) == 0:
            print('{0} is factor of {1}'.format(curr_num, num))
            factors_container.append(curr_num)
        else:
            print('{0} is not factor of number'.format(curr_num))

    return factors_container

var = int(input("Enter number: "))
res = factors_number(var)
print(res)
