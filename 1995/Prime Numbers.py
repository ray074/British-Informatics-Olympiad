def isPrime(num):
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            return False
    return True


limit = int(input("Maximum number to test? "))
primeList = [str(p) for p in range(2, limit) if isPrime(p)]
primes = " ".join(primeList)

print(f"\nThe following numbers between 2 and {limit} are prime:\n")
print(primes)
print(f"\nA total of {len(primeList)} primes numbers were found in this range.")
