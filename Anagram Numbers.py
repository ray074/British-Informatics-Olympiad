def is_anagram(num1, num2):
    return sorted(list(str(num1))) == sorted(list(str(num2)))

def determine_anagram_nums(number):
    digits, digit_list = list(range(2,10)), []
    for num in digits:
        if is_anagram(number, num * number):
            digit_list.append(num)
    
    return " ".join([str(digit) for digit in digit_list]) if len(digit_list) > 0 else 'NO' 

def main():
    print(determine_anagram_nums(int(input())))
    
main()