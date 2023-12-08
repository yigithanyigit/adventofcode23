
from wsgiref.validate import ErrorWrapper


class Game:
    def __init__(self, id, r=0, g=0, b=0) -> None:
        self.id = id
        self.r = r
        self.g = g
        self.b = b

def solve(line):
    r = [12, 13, 14]
    s = 0
    stripped = line.strip("\n ").split(":")
    #print(stripped[1].split(';'))
    game = Game(stripped[0].split()[1])
    for cubes in stripped[1].split(';'):
        for cube in cubes.split(','):
            splitted_cube = cube.split()
            #print(splitted_cube)
            value = splitted_cube[0].strip()
            color = splitted_cube[1].strip()[0]
            ivalue = int(value)
            #print(value, color)
            if color == 'r':
                game.r = max(game.r, ivalue);
            if color == 'g':
                game.g = max(game.g, ivalue);
            if color == 'b':
                game.b = max(game.b, ivalue);
                

    print("ID", game.id, game.r, game.g, game.b)
    return int(game.r) * int(game.b) * int(game.g)
        
    
if __name__ == "__main__":
    sum = 0
    with open("input", "r") as f:
        for line in f:
            sum += solve(line)
            #print(solve(line))
    print(sum)
    