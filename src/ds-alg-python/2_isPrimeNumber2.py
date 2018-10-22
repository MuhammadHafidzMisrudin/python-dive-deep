primes = []

def check_prime_numbers(low, high):
    for isPossiblePrimeNum in range(low, high):
        print("outer loop", isPossiblePrimeNum)
        # assume number is prime until shown it is not.
        isPrime = True
        # check for factors.
        for num in range(2, isPossiblePrimeNum):
            print("inner loop", num)
            if (isPossiblePrimeNum % num) == 0:
                isPrime = False
                print('{0} is {1} and not prime number'.format(isPossiblePrimeNum, isPrime))
                break
        if isPrime:
            # isPrime = True
            print('{0} is {1} and prime number'.format(isPossiblePrimeNum, isPrime))
            primes.append(isPossiblePrimeNum)

check_prime_numbers(2, 10)
print('Prime Numbers: ', primes)
