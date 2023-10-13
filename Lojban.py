lojban = {

    "no": "0",
    "pa": "1",
    "re": "2",
    "ci": "3",
    "vo": "4",
    "mu": "5",
    "xa": "6",
    "ze": "7",
    "bi": "8",
    "so": "9"

}

string, denary = input("Enter: "), []

for i in range(0, len(string), 2):
    denary.append(lojban[string[i:i+2]])
print("".join(denary))