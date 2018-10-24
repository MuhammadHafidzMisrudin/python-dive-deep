def pyramid(num):
    # dashes decrease, stars increase.
    # count up.
    for i in range(1, num, 2):
        print('-'*num+i*'*')
        num = num-1 # dashes decrease.

################################################################################

def pyramidReverse(num_x):
    # dashes increase, stars decrease.
    # count down.
    for i in range(num_x, 0, -2):
        print('-'*num_x+i*'*')
        num_x = num_x+1 # dashes increase.

################################################################################

def rightTriangle(num):
    # stars increase, dashes decrease.
    # count up.
    for i in range(1, num+1, 1):
        print('*'*i+num*'-')
        num = num-1

################################################################################

def rightTriangleReverse(num):
    for i in range(1, num+1, 1):
        print('*'*num+i*'-')
        num = num-1

################################################################################

def rightTriangleMirror(num):
    # dashes increase, stars decrease.
    j = 1
    for i in range(num, 0, -1):
        print('-'*i+j*'*')
        j = j+1

################################################################################

def rightTriangleMirrorReverse(num):
    for i in range(1, num+1, 1):
        print('-'*i+num*'*')
        num = num-1

################################################################################

pyramid(11)
print('\n')
pyramidReverse(11)
print('\n')
rightTriangle(7)
print('\n')
rightTriangleReverse(7)
print('\n')
rightTriangleMirror(7)
print('\n')
rightTriangleMirrorReverse(7)
