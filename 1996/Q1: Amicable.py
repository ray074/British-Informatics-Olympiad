def sum_factors(num):
    return sum([factor for factor in range(1, num) if num % factor == 0])

def main():
    num1, num2 = int(input()), int(input())
    if num1 == num2 or (num1 <= 0 or num2 <= 0): print("Not amicable")
    else: print("Amicable") if sum_factors(sum_factors(num1)) == num1 and sum_factors(num1) == num2 else print("Not amicable")
    
main()
