board = [["." for _ in range(10)] for _ in range(10)]

class Object:
    def __init__(self, x, y, d, kind):
        self.x = x
        self.y = y
        self.d = d
        self.kind = kind
        
    
    def rotate(self, direction):
        directions = ["L", "T", "R", "B"]
        return directions[(directions.index(direction) + 1) % 4]
    

def move(Object):
    
    if Object.d == "T": new_x, new_y = Object.x - 1, Object.y
    if Object.d == "R": new_x, new_y = Object.x, Object.y + 1
    if Object.d == "B": new_x, new_y = Object.x + 1, Object.y
    if Object.d == "L": new_x, new_y = Object.x, Object.y - 1
    
    if not(is_obstacle((new_x, new_y))):
        Object.x, Object.y = new_x, new_y
        reset(Object.kind)
        board[new_x][new_y] = Object.kind
    else:
        Object.d = Object.rotate(Object.d)
            
    
def check(Pigs, Farmer, count, meeting_log, key):
    if (Pigs.x == Farmer.x and Pigs.y == Farmer.y):
        if key == "M":
            meeting_log.append((Pigs.x, Pigs.y, count))
        else:
            board[Pigs.x][Pigs.y] = "+"
        
    
def reset(key):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == key:
                board[i][j] = "."

    
def place_trees(amount):
    for _ in range(amount):
        x, y = (int(i) for i in input("Enter Tree Coordinates: ").split())
        x, y = convert(x, y, "i")
        board[x][y] = "*"
    
    
def print_board():
    print()
    for row in board:
        print(" ".join(row))
    
    
def convert(x, y, d):
    if d == "i":
        return (10-y, x-1)
    return (y+1, 10-x)


def is_obstacle(new_pos):
    x, y = new_pos
    if (0 <= x <= 9 and 0 <= y <= 9) and board[x][y] != "*":
        return False
    return True


def main():
    
    Px, Py = (int(x) for x in input("\nEnter the Coordinates of the Pigs: ").split())
    Fx, Fy = (int(y) for y in input("Enter the Coordinates of the Farmer: ").split())
    (Px, Py), (Fx, Fy) = (convert(Px, Py, "i"), convert(Fx, Fy, "i"))
    Pigs, Farmer, count, meeting_log = Object(Px, Py, "T", "P"), Object(Fx, Fy, "T", "F"), 0, []
    board[Px][Py] = "P" 
    board[Fx][Fy] = "F"
    print_board()
    
    while True:
        try:
            command, num = (x for x in input("\nEnter Command: ").split())
            if command.upper() == "T": place_trees(int(num))
            elif command.upper() == "M":
                for _ in range(int(num)):
                    count += 1
                    move(Pigs)
                    move(Farmer)
                    check(Pigs, Farmer, count, meeting_log, "M")

                if meeting_log:
                    for group in meeting_log:
                        x, y = convert(group[0], group[1], "c")
                        print(f"Farmer and pigs meet on move {group[2]} at ({x},{y})")

                meeting_log.clear()
            
            check(Pigs, Farmer, count, meeting_log, "S")
            print_board()
            reset("+")
    
        except ValueError:
            return

if __name__ == "__main__":
    main()
