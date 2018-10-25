# The Highest Common Factor (H.C.F) of two (or more) numbers is the largest number that divides evenly into both numbers.

list_hcf = []
def computeHCF(num1, num2):

    smallerNum = 0
    hcf = 0
    if num1 > num2:
        smallerNum = num2
    else:
        smallerNum = num1

    for i in range(1, smallerNum+1):
        if ((num1%i == 0) and (num2%i == 0)):
            hcf = i
            list_hcf.append(hcf)

    return hcf


def GCD(a, b):
    if (a == 0) or (b == 0):
        return -1

    if (a == 1) or (b == 1):
        return 1

    while a > 0 and b > 0:
        if a > b:
            a %= b
        else:
            b %= a
        print('a = {0}'.format(a))
        print('b = {0}'.format(b))
    print('(a == 0 and b or a) => ', a == 0 and b or a)
    return 0 == a and b or a


x = 300
y = 120
print('\n')
print('the highest common factor = {0}'.format(computeHCF(x, y)))
print('output list = ', list_hcf)
print('\n')
print('result from GCD() = ', GCD(x,y))
print('\n')
