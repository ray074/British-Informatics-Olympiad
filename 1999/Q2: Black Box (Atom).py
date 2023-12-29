class Ray:
    def __init__(self, x, y, d, state):
        self.x = x
        self.y = y
        self.d = d
        self.state = state
        
    
    @staticmethod
    def rotate(ray, new_pos, atom_pos, box):
        neighbours = get_neighbours(new_pos)
        
        if ray.d == "T" or ray.d == "B":
            for i in range(len(box)):
                if box[i][ray.y] == "A" and (i, ray.y) in neighbours:
                    box[i][ray.y] = "*"
                    if ray.d == "T": box[i+1][ray.y] = "+"
                    if ray.d == "B": box[i-1][ray.y] = "+"
                    ray.state = "Absorbed"
                    return
            
        elif ray.d == "R" or ray.d == "L":
            for j in range(len(box[0])):
                if box[ray.x][j] == "A" and (ray.x, j) in neighbours:
                    box[ray.x][j] = "*"
                    if ray.d == "R": box[ray.x][j-1] = "+"
                    if ray.d == "L": box[ray.x][j+1] = "+"
                    ray.state = "Absorbed"
                    return
    
        ray.state = "Deflected"
        new_x, new_y = new_pos
        atom_x, atom_y = atom_pos
        
        if new_x < atom_x: return "T"
        if new_x > atom_x: return "B"
        if new_y < atom_y: return "L"
        if new_y > atom_y: return "R"

        
def move(ray, box):
    if ray.d == "T": new_x, new_y = ray.x - 1, ray.y
    if ray.d == "B": new_x, new_y = ray.x + 1, ray.y
    if ray.d == "R": new_x, new_y = ray.x, ray.y + 1
    if ray.d == "L": new_x, new_y = ray.x, ray.y - 1
    
    check((new_x, new_y), ray, box)

    if ray.state is None:
        ray.x, ray.y = new_x, new_y
        box[ray.x][ray.y] = "+"
    
    elif ray.state == "Deflected":
        ray.state = None


def check(new_pos, ray, box):
    x, y = new_pos
    neighbours = get_neighbours(new_pos)
    
    if x < 0 or x > 9 or y < 0 or y > 9:
        ray.state = "Exited"
        return
    
    elif box[x][y] == "A":
        ray.state = "Absorbed"
        box[x][y] = "*"
            
    else:
        for n in neighbours:
            if box[n[0]][n[1]] == "A":
                ray.d = Ray.rotate(ray, new_pos, (n[0], n[1]), box)
                break
            
    
def get_neighbours(new_pos):
    x, y = new_pos
    neighbours = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    neighbours = [t for t in neighbours if 0 <= t[0] <= 9 and 0 <= t[1] <= 9]
    return neighbours


def calc_start_and_d(direction, num):
    if direction == "T": return (0, num-1, "B")
    if direction == "B": return (9, num-1, "T")
    if direction == "R": return (10-num, 9, "L")
    if direction == "L": return (10-num, 0, "R")
    
    
def convert(x, y, d):
    if d == "i":
        return (10 - y, x - 1)
    
    if x == 0: return ("T", y+1)
    if x == 9: return ("B", y+1)
    if y == 0: return ("L", 10-x)
    if y == 9: return ("R", 10-x)


def reset(box):
    for i in range(len(box)):
        for j in range(len(box[0])):
            if box[i][j] == "+":
                box[i][j] = "."
            elif box[i][j] == "*":
                box[i][j] = "A"


def print_box(box):
    print()
    for row in box:
        print(" ".join(row))
   
   
def determine_result(ray, start_x, start_y):
    if ray.state == "Exited":
        exit_x, exit_y = convert(ray.x, ray.y, "c")
        if (ray.x, ray.y) == (start_x, start_y):
            print("Reflected")
        else:
            print(f"Exits at {exit_x} {exit_y}")
    else:
        print(ray.state)
    
    
def main():
    box = [["." for _ in range(10)] for _ in range(10)]
    print()
    
    for i in range(5):
        x, y = (int(x) for x in input(f"Enter Coordinates of Atom {i+1}: ").split())
        x, y = convert(x, y, "i")
        box[x][y] = "A"
   
    print_box(box)
   
    while True:
        direction, num = input("\nEnter Ray Entry Point: ").split()
        ray, num = Ray("-1", "-1", None, None), int(num)
       
        if direction != "X":
            start_x, start_y, ray.d = calc_start_and_d(direction, num)
            ray.x, ray.y = start_x, start_y
            box[ray.x][ray.y] = "+"
            
            while ray.state in [None, "Deflected"]:
                move(ray, box)
                
            print_box(box)
            determine_result(ray, start_x, start_y)
            reset(box)
            
        elif direction == "X" and num == 0:
            return


if __name__ == "__main__":
    main()
