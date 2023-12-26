def find_digit_letter(string):
    numbers = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]
    
    for number in numbers:
        score = 0
        for letter in number:
            if letter in string:
                score += 1
        if score == len(number):
            return number
    
    return "NO"


def convert(string):
    num_dict = {"ONE": 1, "TWO": 2, "THREE": 3, "FOUR": 4, "FIVE": 5, "SIX": 6, "SEVEN": 7, "EIGHT": 8, "NINE": 9}
    return num_dict[string] if string != "NO" else "NO"
    

def check(number, string):
    index_dict, path = {}, []
    
    for i in range(len(string)):
        if string[i] in number and string[i] not in index_dict:
            index_dict[string[i]] = [i]
        elif string[i] in number and string[i] in index_dict:
            index_dict[string[i]].append(i)
            
    for letter in number:
        indexes = index_dict[letter]
        for index in indexes:
            if len(path) == 0 or index > path[-1]:
                path.append(index)
                break

    return number if len(path) == len(number) else "NO"
    
    
def main():
    string = input("Enter Digit Letter String: ").upper()
    number = find_digit_letter(string)
    print(convert(check(number, string))) if number != "NO" else print("NO")
    

main()
