def calc_colour(l1, l2):
    colour_set = {"R", "G", "B"}
    return l1 if l1 == l2 else list(colour_set - set(list(l1 + l2)))[0]

def find_final_colour(str_list):
    new_list = []
    
    while len(str_list) > 1:
        for i in range(len(str_list) -1):
            new_list.append(calc_colour(str_list[i], str_list[i+1]))
        str_list = new_list.copy()
        new_list.clear()
    else:
        return str_list[0].upper()

def main():
    str_list = [letter.upper() for letter in str(input())]
    res = find_final_colour(str_list)
    print(res)
    
main()