def time_to_words(hours, mins, edge_cases={"0", "1", "15", "30", "45", "59"}):
    nums = {
    "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven",
    "8": "eight", "9": "nine", "10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen",
    "14": "fourteen", "15": "fifteen", "16": "sixteen", "17": "seventeen", "18": "eighteen",
    "19": "nineteen", "20": "twenty", "21": "twenty-one", "22": "twenty-two", "23": "twenty-three",
    "24": "twenty-four", "25": "twenty-five", "26": "twenty-six", "27": "twenty-seven", "28": "twenty-eight",
    "29": "twenty-nine", "30": "thirty", "31": "thirty-one", "32": "thirty-two", "33": "thirty-three",
    "34": "thirty-four", "35": "thirty-five", "36": "thirty-six", "37": "thirty-seven", "38": "thirty-eight",
    "39": "thirty-nine", "40": "forty", "41": "forty-one", "42": "forty-two", "43": "forty-three",
    "44": "forty-four", "45": "forty-five", "46": "forty-six", "47": "forty-seven", "48": "forty-eight",
    "49": "forty-nine", "50": "fifty", "51": "fifty-one", "52": "fifty-two", "53": "fifty-three",
    "54": "fifty-four", "55": "fifty-five", "56": "fifty-six", "57": "fifty-seven", "58": "fifty-eight",
    "59": "fifty-nine"
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
