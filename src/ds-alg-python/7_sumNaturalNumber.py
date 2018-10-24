container = []

def sumNumbers(num):
    sumNum = 0
    while (num > 0):
        sumNum += num
        container.append(sumNum)
        print('Number: {0}'.format(num))
        num -= 1

    return sumNum

print('total number: ', sumNumbers(10))
print(container)
print('\n')

################################################################################

def recursionSumNumbers(num):
    res = 0
    if num <= 0:
        res = num
    else:
        print('current number: {0}.'.format(num))
        res  = num + recursionSumNumbers(num - 1)
        print('current recursion res: {0}.'.format(res))

    return res


print('result: ', recursionSumNumbers(5))
