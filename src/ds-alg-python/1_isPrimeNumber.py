primes = []

def check_prime_numbers(low, high):
    # iterate from the low to high.
    for isPossiblePrimeNum in range(low, high):
        print('outer loop', isPossiblePrimeNum)
        # check all possible number is greater than 1.
        if isPossiblePrimeNum > 1:
            # iterate through from 2 until current possible number.
            # check for factors.
            for i in range(2, isPossiblePrimeNum):
                print('inner loop', i)
                if (isPossiblePrimeNum % i) == 0:
                    print('{0} is not prime'.format(isPossiblePrimeNum))
                    break
            else: # loop not exited via break.
                print('prime number: ', isPossiblePrimeNum)
                primes.append(isPossiblePrimeNum)


check_prime_numbers(2, 20)
print(primes)
