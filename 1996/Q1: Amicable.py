def sum_factors(num):
    return sum([factor for factor in range(1, num-1) if num % factor == 0])

def main():
    num1, num2 = int(input()), int(input())
    print("Amicable") if num1 == sum_factors(sum_factors(num1)) and num1 != num2 else print("Not amicable")
    
main()
