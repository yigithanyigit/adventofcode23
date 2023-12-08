from pickle import TRUE
from re import S
import string

def make_matrix(line, matrix):
    line = line.strip()
    matrix.append(line)

def solve(matrix):
    adj = []
    special = '*'
    m = [[False for _ in matrix[0]] for _ in matrix]
    s = 0
    for r_idx, row in enumerate(matrix):
        for r_c_idx, ch in enumerate(row):
            if ch != '.' and not ch.isnumeric():
                # symbol found
                adj = find_adjacent_points(matrix, (r_idx, r_c_idx))
                # special symbol found
                if ch == special:
                    special_s = []
                    for point in adj: 
                        if matrix[point[0]][point[1]].isnumeric() is True:
                            # because of my find function which is returns 0 as empt we cannot achive special_s as 2 
                            # for example:
                            # [35, 467, 0] result
                            # [35, 467] supposed to be
                            res = find(matrix, point,(r_idx, r_c_idx),  m)
                            if res != 0:
                                special_s.append(res)
                    if len(special_s) == 2:
                        s += special_s[0] * special_s[1]
            """
                    else:
                        for v in special_s:
                            s += v
                else: 
                    for point in adj: 
                        if matrix[point[0]][point[1]].isnumeric() is True:
                            s += find(matrix, point,(r_idx, r_c_idx),  m)
            """
    return s
                
                
def find_adjacent_points(matrix, point):

  rows = len(matrix)
  cols = len(matrix[0])
  
  adjacent_points = []
  
  directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]

  for direction in directions:
    
    adjacent_row = point[0] + direction[0]
    adjacent_col = point[1] + direction[1]

    if 0 <= adjacent_row < rows and 0 <= adjacent_col < cols:
      adjacent_points.append((adjacent_row, adjacent_col))

  return adjacent_points
    
        
        
def find(matrix, point, symbol_point, map):
    # find that where to start number
    row = point[0]
    column = point[1]
    idx = column
    if column <= symbol_point[1]:
        counter = 0
        for ch in reversed(matrix[row][0:column]):
            if ch.isnumeric() is True:
                counter += 1
            else:
                break
        #print(counter)
        idx = column - counter
    else:
        pass
    
        
    s = ''
    for i, ch in enumerate(matrix[row][idx::]):
        if ch.isnumeric() is True and map[row][i + idx] is False:
            s += ch
            map[row][i + idx] = True
        else:
            break
        
    if s == '':
        return 0
    else:
        return int(s)
    

if __name__ == "__main__":
    sum = 0
    matrix = []
    with open("input", "r") as f:
        for line in f:
            make_matrix(line, matrix)
            #print(solve(line))
        print(solve(matrix))