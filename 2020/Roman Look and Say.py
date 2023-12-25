def look_and_say(string):
    split_str = split(string)
    singles, romans, final = [group[0] for group in split_str], [], []
    
    for block in split_str:
        romans.append(convert(len(block)))
    
    for count, roman in zip(romans, singles):
        final.append(count + roman)
        
    res = "".join(final)
    return res


def convert(value):
    numerals = {
    
        1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
        10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
        100: 'C', 400: 'CD', 500: 'D', 900: 'CM',
        1000: 'M'
    }

    nums = [x for x in sorted(numerals, reverse=True)]
    romans = []

    while value != 0:
        for num in nums:
            if num <= value:
                value -= num
                romans.append(numerals[num])
                break
    
    conv = "".join(romans)
    return conv
    
    
def split(string):
    temp, res = [], []
    for char in list(string):
        if len(temp) == 0 or char in temp:
            temp.append(char)
        else:
            res.append("".join(temp))
            temp.clear()
            temp.append(char)
    
    res.append("".join(temp))
    return res


def main():
    string, n = input("Enter Roman Numeral and n value: ").split()
    
    for _ in range(int(n)):
        string = look_and_say(string)
        
    i_count, v_count = string.count("I"), string.count("V")
    print(i_count, v_count)
    
    
main()
