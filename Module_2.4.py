numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
for primes in range(len(numbers)):
    if primes > 1:
        for i in range(2, primes):
            if(primes % i) == 0:
                break
            else:
                print(primes)
