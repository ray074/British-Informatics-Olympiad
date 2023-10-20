def gen_lucky_nums():
    lucky_nums, n = [num for num in range(10002) if num % 2 != 0], 3
    while n < lucky_nums[-1]:
        lucky_nums = remove(lucky_nums, n)
        i = lucky_nums.index(n)
        n = lucky_nums[i+1]
    return lucky_nums
    
def remove(num_list, n):
    pos = n - 1
    while pos < len(num_list) - 1:
        num_list.pop(pos)
        pos += n - 1
    return num_list
    
def locate(lucky_nums, num, values = []):
    for i in range(num-1, 0, -1):
        if i in lucky_nums:
            values.append(str(i))
            break
    for j in range(num+1, 10002):
        if j in lucky_nums:
            values.append(str(j))
            break
    return " ".join(values)
    
def main():
    num = int(input())
    lucky_nums = gen_lucky_nums()
    print(locate(lucky_nums, num))
    
main()
