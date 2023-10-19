from itertools import combinations

def is_prime(num):
    if num < 2:
        return False
    for divisor in range(2, int(num ** 0.5) + 1):
        if num % divisor == 0:
            return False
    return True

def find_pairs(prime_list, target):
    count = 0
    combs = combinations(prime_list, 2)
    for comb in combs:
        if sum(comb) == target:
            count += 1
    if is_prime(target / 2):
        count += 1
    
    return count

def main():
    limit = int(input())
    prime_list = [prime for prime in range(2, limit + 1) if is_prime(prime)]
    print(find_pairs(prime_list, limit))
    
main()
