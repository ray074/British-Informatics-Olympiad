def calc_isbn(string, q_index, edge_case):
    string = string.replace("?", "0")
    multipliers, nums_list = list(range(10, 0, -1)), [int(x) for x in str(string)]
    total, count = 0, 0
    
    for multiplier, num in zip(multipliers, nums_list):
        total += multiplier * num 
    
    if edge_case == 1:
        total -= 10
    elif edge_case == 2:
        total += 10
    
    while total % 11 != 0:
        count += 1
        total += multipliers[q_index]
    return "X" if count == 10 else count


def main():
    string = input()
    string_list = [str(x) for x in string]
    q_index = string_list.index("?")
    if string_list[0] == "0":
        string_list[0] = "1"
        result = calc_isbn("".join(string_list), q_index, 1)
    elif string_list[-1] == "X":
        string_list[-1] = "0"
        result = calc_isbn("".join(string_list), q_index, 2)
    else:
         result = calc_isbn(string, q_index, False)
    
    print(result)
    

main()

