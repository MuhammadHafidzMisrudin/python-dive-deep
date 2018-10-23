total_num = []

def factorial_number(x_num):

    # if num = 6.
    # exp: 6! = 6*5*4*3*2*1 = 720.

    res_factorial = 1
    if x_num < 0:
        res_factorial = -1
        total_num.append(res_factorial)
        return 'factorial must be a positive integer number, {0}'.format(res_factorial)

    if x_num == 0:
        res_factorial = 1
        total_num.append(res_factorial)
        return '{0} factorial is {1}'.format(x_num, res_factorial)

    for i in range(1, x_num + 1):
        res_factorial = (res_factorial * i)
        total_num.append(res_factorial)

    return res_factorial



getInput = int(input('get input: '))
total = factorial_number(getInput)
print(total_num)
print('total: {0}'.format(total))
