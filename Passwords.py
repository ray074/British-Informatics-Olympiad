#All from @Pararcana

def check_passwords(string):
    for i in range(len(string) - 1):
        if string[i:i+1] == string[i+1:i+2]:
            return 'Rejected'
    for j in range(len(string) - 3):
        if string[j:j+2] == string[j+2:j+4]:
            return 'Rejected'
    for v in range(len(string) - 5):
        if string[v:v+3] == string[j+3: j+6]:
             return 'Rejected'
    for x in range(len(string) - 7):
        if string[x:x+4] == string[x+4: x+8]:
            return 'Rejected'
   
    return 'Accepted'


def main():
    string = input()
    print(check_passwords(string))

main()