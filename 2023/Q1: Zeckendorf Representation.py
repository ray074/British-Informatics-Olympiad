def gen_fib(num):
    a, b = 1, 2
    fib_list = [a, b]
    while a + b <= num:
        fib_list.append(a+b)
        a, b = b, a + b
    return sorted(fib_list, reverse=True)
            
def zeckendorf_repr(fib_list, num):
    nums = []
    while num != 0:
        for value in fib_list:
            if value <= num:
                num -= value
                nums.append(value)
                break
    return [str(x) for x in nums]

def main():
    num = int(input())
    fib_list = gen_fib(num)
    print(" ".join(zeckendorf_repr(fib_list, num)))
    
main()
