num = 10


def drawPerfectSquare(numStars):
    print('*'*numStars)
    for i in range(numStars-2):
        print('*'*(numStars))
    print('*'*numStars)

def drawSquareHollow(numStars):
    print('*'*numStars)
    for i in range(numStars-2):
        print('*'+(numStars-2)*' '+'*')
    print('*'*numStars)

print('\n')
drawPerfectSquare(num)
print('\n')
drawSquareHollow(num)
print('\n')
