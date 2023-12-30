
def encode_and_decode(left_grid, right_grid, word, action):
    if action == "Encode":
        if len(word) % 2 == 1: word += "X"
    
    chunks, final = [], []
    
    for i in range(0, len(word), 2):
        chunks.append(word[i:i+2])
   
    for block in chunks:
        indexes = []
       
        for i in range(5):
            for j in range(5):
                if left_grid[i][j] == block[0]: indexes.append((i, j))

        for i in range(5):
            for j in range(5):
                if right_grid[i][j] == block[1]: indexes.append((i, j))

        if indexes[0][0] == indexes[1][0]:
            if action == "Encode":
                final.append(left_grid[indexes[0][0]][(indexes[0][1] + 1) % 5])
                final.append(right_grid[indexes[1][0]][(indexes[1][1] + 1) % 5])
            else:
                final.append(left_grid[indexes[0][0]][(indexes[0][1] - 1) % 5])
                final.append(right_grid[indexes[1][0]][(indexes[1][1] - 1) % 5])
        else:
            final.append(left_grid[indexes[1][0]][indexes[0][1]])
            final.append(right_grid[indexes[0][0]][indexes[1][1]])

    text = "".join(final)
    if action == "Decode" and text[-1] == "X": text = text[0:len(text)-1]
    return text


def generate_grids(words):
    return (create_matrix(words[0], "Forward"), create_matrix(words[1], "Reverse"))


def create_matrix(word, direction):
    alpha = list("ABCDEFGHIJKLMNOPRSTUVWXYZ")
    new, temp, grid, reverse = "", [], [], []

    for letter in list(word):
        if letter not in new:
            new += letter
           
    for letter in alpha:
        if letter not in new:
            new += letter

    for char in list(new):
        temp.append(char)
        if len(temp) == 5:
            grid.append(temp.copy())
            temp.clear()
           
    if direction == "Forward":
        return grid
    else:
        for i in range(len(grid) - 1, -1, -1):
            letters = grid[i]
            for x in range(len(letters) - 1, -1, -1):
                temp.append(grid[i][x])
               
                if len(temp) == 5:
                    reverse.append(temp.copy())
                    temp.clear()
       
        return reverse


def print_grids(left_grid, right_grid):
    print()
    for i in range(5):
        print(f"{'  '.join(left_grid[i])} \t\t {'  '.join(right_grid[i])}")
    print()


def main():
    words = []
    print()
    for _ in range(2):
        words.append(input("Enter key-word: ").upper())
   
    left_grid, right_grid = generate_grids(words)  
    print_grids(left_grid, right_grid)

    while True:
        choice = input("\nEnter choice: ").upper()
        if choice == "E":
            word = input("Enter word to Encode: ").upper()
            print(encode_and_decode(left_grid, right_grid, word, "Encode"))
       
        elif choice == "D":
            word = input("Enter word to Decode: ").upper()
            print(encode_and_decode(left_grid, right_grid, word, "Decode"))
       
        elif choice == "Q":
            return


if __name__ == "__main__":
    main()
