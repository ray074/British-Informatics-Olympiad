def rivers(start):
    river_list = [int(start)]
    
    while int(start) < 50000:
        start_value = int(start)
        ints = [int(num) for num in str(start)]
        total = 0
        for num in ints:
            total += num
        start_value += total
        river_list.append(start_value)
        start = start_value
        
    return river_list


def main():
    river = input("Enter River: ")
    result = rivers(river)
    for number in result:
        if number in rivers(1):
            print(f"First meets river 1 at {number}")
            break
        elif number in rivers(3):
            print(f"First meets river 3 at: {number}")
            break
        elif number in rivers(9):
            print(f"First meets river 9 at: {number}")
            break

main()
