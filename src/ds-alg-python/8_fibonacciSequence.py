seq_cont = []

def printFibonacciNum(num):
    numOne = 0
    numTwo = 1
    counter = 2

    if num < 0:
        print('must be a positive integer')
    elif num == 0:
        print('fibonacci sequence up to  {0}th= {1}'.format(num, numOne))
        return numOne
    elif num == 1:
        print('fibonacci sequence up to  {0}th= {1}'.format(num, numTwo))
        return numTwo
    else:
        while (counter < num+1):
            # print(counter)
            sumNum = numOne+numTwo
            numOne = numTwo
            numTwo = sumNum
            print('{0}th= {1}'.format(counter, numTwo), end=', ')
            seq_cont.append(numTwo)
            counter += 1


printFibonacciNum(9)
print('result: ', seq_cont)
print('\n')
################################################################################

container = []
def fibonacciRecursion(num):
    if num < 0:
        print('must be a positive integer')
    elif num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        n1 = fibonacciRecursion(num-1)
        n2 = fibonacciRecursion(num-2)
        res = fibonacciRecursion(num-1) + fibonacciRecursion(num-2)
        container.append(n2)
        return res

input = 9
fibonacciRecursion(input)
for i in range(0, input+1):
    print(print('recursion of {0}th, result= {1} '.format(i, fibonacciRecursion(i))))
