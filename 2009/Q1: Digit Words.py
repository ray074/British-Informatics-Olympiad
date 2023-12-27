numbers = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"]

def find_digit_word(string):
    for number in numbers:
        score = 0
        for letter in number:
            if letter in string:
                score += 1
        if score == len(number):
            return number

    return "NO"


def convert(string):
    return numbers.index(string) + 1 if string in numbers else "NO"


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
    string = input("Enter Digit Word: ").upper()
    for string in strings:
      number = find_digit_word(string)
      print(convert(check(number, string))) if number != "NO" else print("NO")


main()
