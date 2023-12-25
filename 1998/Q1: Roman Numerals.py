numerals = {
    
    1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
    10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
    100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
    1000: 'M'
}

nums = [num for num in sorted(numerals, reverse=True)]
inp = int(input())

romans = []

while inp != 0:
    for num in nums:
        if num <= inp:
            inp -= num
            romans.append(numerals[num])
            break

print("".join(romans))
