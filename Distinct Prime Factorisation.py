def is_prime(num):
    if num < 2:
        return False
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            return False
    return True

def product_of_primes(num):
    factors, total = set(), 1
    for factor in range(1, num + 1):
        if num % factor == 0 and is_prime(factor):
            factors.add(factor)
    for value in factors:
        total *= value
    return total

def main():
    num = int(input())
    print(product_of_primes(num))

main()