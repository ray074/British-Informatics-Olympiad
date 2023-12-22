board = [["." for _ in range(11)] for _ in range(11)]

class Ant:
    def __init__(self, x, y, d, removed):
        self.x = x
        self.y = y
        self.d = d
        self.removed = False

    @staticmethod
    def rotate(d, new_pos):
        directions = ["L", "T", "R", "B"]
        x, y = new_pos

        if board[x][y] == ".":
            return directions[(directions.index(d) + 1) % 4]
        else:
            return directions[directions.index(d) - 1]
        
        
def outOfBounds(x, y):
    if 0 <= x <= 10 and 0 <= y <= 10:
        return False
    return True
        
        
def convert(x, y, d):    
    if d == "i":
        return (11-y, x-1)
    return (y+1, 11-x)


def manipulate(Ant):
    
    if Ant.d == "T": new_x, new_y = Ant.x - 1, Ant.y
    if Ant.d == "R": new_x, new_y = Ant.x, Ant.y + 1
    if Ant.d == "B": new_x, new_y = Ant.x + 1, Ant.y
    if Ant.d == "L": new_x, new_y = Ant.x, Ant.y - 1
    
    if not(outOfBounds(new_x, new_y)):
        Ant.x, Ant.y, Ant.d = new_x, new_y, Ant.rotate(Ant.d, (new_x, new_y))
        if board[new_x][new_y] == ".":
            board[new_x][new_y] = "*"
        else:
            board[new_x][new_y] = "."
    else:
        Ant.removed = True
    
    
def main():
    
    print("Welcome to the Ants Simulation")
    print("Enter the Coordinates and Directions of the Ants in this form: 5 5 T ")
    print("Enter -1 to exit \n")
    
    x1, y1, d1 = (x for x in input("Enter Ant 1 Coordinates and Direction: ").split())
    x2, y2, d2 = (y for y in input("Enter Ant 2 Coordinates and Direction: ").split())
    x1, y1 = convert(int(x1), int(y1), "i")
    x2, y2 = convert(int(x2), int(y2), "i")
    Ant1, Ant2 = Ant(x1, y1, d1, False), Ant(x2, y2, d2, False)
    
    while True:
        moves = int(input("\nEnter number of moves to calculate: "))
        if moves != -1:
            for _ in range(moves):
                if not(Ant1.removed): manipulate(Ant1)
                if not(Ant2.removed): manipulate(Ant2)
                
            for row in board:
                print(" ".join(row))
                
            A1x, A1y = convert(Ant1.x, Ant1.y, "c")
            A2x, A2y = convert(Ant2.x, Ant2.y, "c")
            
            print(A1x, A1y, Ant1.d) if not(Ant1.removed) else print("Removed")
            print(A2x, A2y, Ant2.d) if not(Ant2.removed) else print("Removed")
        
        else:
            return
    
    
if __name__ == "__main__":
    main()
