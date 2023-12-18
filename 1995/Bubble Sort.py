nums = []
print("Type in up to 20 numbers, ending with -999\n")

for _ in range(20):
    value = int(input("Enter number: "))
    if value != -999:
        nums.append(value)
    else:
        break
        
print(f"\nThe {len(nums)} sorted numbers are: \n")
print(" ".join(str(num) for num in sorted(nums)))
