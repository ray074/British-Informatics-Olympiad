def time_to_words(hours, mins, edge_cases={"0", "1", "15", "30", "45", "59"}):
    nums = {
    "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven",
    "8": "eight", "9": "nine", "10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen",
    "14": "fourteen", "16": "sixteen", "17": "seventeen", "18": "eighteen",
    "19": "nineteen", "20": "twenty", "21": "twenty-one", "22": "twenty-two", "23": "twenty-three",
    "24": "twenty-four", "25": "twenty-five", "26": "twenty-six", "27": "twenty-seven", "28": "twenty-eight",
    "29": "twenty-nine"
}

    if mins == "0": return f"{hours} o'clock"
    if mins == "1": return f"one minute past {nums[hours]}"
    if mins == "15": return f"quarter past {nums[hours]}"
    if mins == "30": return f"half past {nums[hours]}"
    if mins == "45": return f"quarter to {nums[str(int(hours) + 1 if int(hours) < 12 else '1')]}"
    if mins == "59": return f"one minute to {nums[str(int(hours) + 1 if int(hours) < 12 else '1')]}"
    
    if mins not in edge_cases:
        if int(mins) in range(1, 30):
            return f"{nums[mins]} minutes past {nums[hours]}"
        else:
            return f"{nums[str(60 - int(mins))]} minutes to {nums[str(int(hours) + 1 if int(hours) < 12 else '1')]}"
    
def main():
    hours, mins = input("Hours: "), input("Minutes: ").replace("00", "0")
    string = time_to_words(hours, mins)
    print(string.capitalize())
    
main()
