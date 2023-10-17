def find_fib_letter(v1, v2, n):
    alpha, rev = {chr(65 + i): i + 1 for i in range(26)}, {i: chr(64 + i) for i in range(1, 27)}
    fib_list = [alpha[v1], alpha[v2]]
    
    while len(fib_list) < 1000000:
        total = alpha[v1] + alpha[v2]
        while total > 26:
            total -= 26
        fib_list.append(total)
        v1 = v2
        v2 = rev[total]
    
    fib_list = [rev[value] for value in fib_list]
    return fib_list[n-1]
    
def main():
    v1, v2, n = input().upper().split()
    print(find_fib_letter(v1, v2, int(n)))
    
main()