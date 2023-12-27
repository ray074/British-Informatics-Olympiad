board = [["." for _ in range(11)] for _ in range(11)]


def play(board):
    temp_board = [["." for _ in range(11)] for _ in range(11)]
    
    for x in range(len(board)):
        for y in range(len(board[0])):
            cur_square = board[x][y]
            neighbours, on_count = get_neighbours(x, y), 0
            
            for group in neighbours:
                if board[group[0]][group[1]] == "0":
                    on_count += 1
                    
            if (cur_square == "0" and on_count in [2,3]) or (cur_square == "." and on_count == 3):
                temp_board[x][y] = "0"
            else:
                temp_board[x][y] = "."
                
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] = temp_board[i][j]


def get_neighbours(x, y):
    neighbours = [
        (x-1,y), (x+1,y), (x,y-1), (x,y+1),
        (x+1,y+1), (x-1,y-1), (x-1,y+1), (x+1,y-1)
    ]
    
    neighbours = [t for t in neighbours if (0 <= t[0] <= 10 and 0 <= t[1] <= 10)]
    return neighbours


def set_up():
    gen0, positions = [], []
    
    for x in range(5):
        gen0.extend(list(input(f"Enter Row {x+1} of Generation 0: ")))

    for i in range(3, 8):
        for j in range(3, 8):
            positions.append((i, j))
            
    for pos, char in zip(positions, gen0):
        board[pos[0]][pos[1]] = char
        
    print()
    for row in board:
        print(" ".join(row))
        
        
def print_board():
    for row in board:
        print(" ".join(row))


def main():
    print("""
Welcome to the Game of Life
Enter Generation 0 with no spaces between characters
The Command "#" with number "n" calculates Generation "n"
The Command "+" with number "n" calculates "n" generations on from the last generation shown
The Command "-" with number 1 terminates the program
""")
    
    set_up()
    cur_gen = 0
    
    while True:
        inp = input("\nEnter Command and Number: ")
        command, num = inp[0], int(inp[1:])
        
        if command == "+":
            for _ in range(num):
                cur_gen += 1
                play(board)
            print_board()
            
        elif command == "#":
            for _ in range(num - cur_gen):
                cur_gen += 1
                play(board)
            print_board()
        
        elif command == "-" and num == 1:
            return
        
if __name__ == "__main__":
    main()
