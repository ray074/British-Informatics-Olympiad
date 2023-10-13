def decrypt(string):
    alpha = {chr(i): i - ord('A') + 1 for i in range(ord('A'), ord('Z') + 1)}
    rev_alpha = {v:k for k,v in alpha.items()}
    str_list = [letter for letter in str(string)]
    final = [str_list[0]]
    
    if len(string) > 1:
        for i in range(1, len(str_list)):
            num1, num2 = alpha[str_list[i]], alpha[str_list[i-1]]
            sub = num1 - num2
            while sub <= 0:
                sub += 26             
            final.append(rev_alpha[sub])
        return final
    return string
    
def main():
    string = input().upper()
    res = decrypt(string)
    print("".join(res))

main()
