from dataclasses import dataclass

@dataclass
class Cell:
    row: int
    col: int

class Excel:
    def __init__(self):
        self.size = 50 +1 
        self.matrix = [["EMPTY"] * self.size for _ in range(self.size)]
        self.parents = [[ Cell(row,col) for col in range(self.size)] for row in range(self.size) ]

        
    def find_parent(self, row, col):
        if self.parents[row][col].row == row and self.parents[row][col].col == col:
            return self.parents[row][col]
        
        parent = self.find_parent(self.parents[row][col].row, self.parents[row][col].col)
        self.parents[row][col] = parent
        return parent

    
    def update(self, row, col, value):
        parent = self.find_parent(row,col)
        self.matrix[parent.row][parent.col] = value
        pass
    
    
    def update_substitution(self, value1, value2):
        # for original in originals:
        #     if self.matrix[original[0]][original[1]] == value1:
        #         self.matrix[original[0]][original[1]] = value2
        for row in range(1, self.size):
            for col in range(1, self.size):
                if self.matrix[row][col] == value1:
                    self.matrix[row][col] = value2
        
    
    def merge(self, r1, c1, r2, c2):
        
        if r1 == r2 and c1 == c2 :
            return
        
        p1 = self.find_parent(r1, c1)
        p2 = self.find_parent(r2, c2)
        
        if self.matrix[p1.row][p1.col] != "EMPTY":
            self.parents[p2.row][p2.col] = p1
        else:
            self.parents[p1.row][p1.col] = p2

        
    def unmerge(self, r, c):
        
        merged = []
        
        p = self.find_parent(r, c)
        value = self.matrix[p.row][p.col]
        
        for row in range(1, self.size):
            for col in range(1, self.size):
                pi = self.find_parent(row,col)
                if p == pi :
                    merged.append(Cell(row,col))
                    
        for cell in merged:
            self.matrix[cell.row][cell.col] = "EMPTY"
            self.parents[cell.row][cell.col] = Cell(cell.row,cell.col)        
        
        self.matrix[r][c] = value
        return
    
    
    def print_cell(self, r,c):
        p = self.find_parent(r,c)
        return self.matrix[p.row][p.col]
    
def solution(commands):
    answer = []
    excel = Excel()
    
    for command in commands:
        tokens = command.split()
        action = tokens[0]
        
        if action == "UPDATE":
            if len(tokens) == 4:
                excel.update(int(tokens[1]), int(tokens[2]), tokens[3])
            else:
                excel.update_substitution(tokens[1], tokens[2])
        
        elif action == "MERGE":
            excel.merge(int(tokens[1]), int(tokens[2]), int(tokens[3]), int(tokens[4]))

        elif action == "UNMERGE":
            excel.unmerge(int(tokens[1]), int(tokens[2]))
        elif action == "PRINT":
            answer.append(excel.print_cell(int(tokens[1]), int(tokens[2])))

    

    return answer