import random


class Deminer:
    
    def __init__(self, dimensions: tuple[int], mine_percentage: int):
        self.dimensions = dimensions
        self.mines_grid = self.generate_mines_grid(mine_percentage)
        self.exploration_grid = self.generate_exploration_grid()

        self.is_explosed = False

    def generate_mines_grid(self, percentage: int) -> list[list[int]]:
        grid = []

        for i in range(self.dimensions[0]):
            line = []
            for j in range(self.dimensions[1]):
                n = random.randint(0, 100)

                if n >= percentage:
                    line.append(0)
                
                else:
                    line.append(1)

            grid.append(line)
        
        return grid
    
    def generate_exploration_grid(self) -> list[list[str]]:
        return [["nothing" for j in range(self.dimensions[1])] for i in range(self.dimensions[0])]
    
    def explore_place(self, i: int, j: int):
        if self.exploration_grid[i][j] == "reported":
            print("This place is reported, please unreport it before explore it")
            return

        if self.mines_grid[i][j]:
            self.is_explosed = True
            return
        
        self.exploration_grid[i][j] = "explored"
    
    def report_mine(self, i: int, j: int):
        self.exploration_grid[i][j] = "reported"
    
    def cancel_report(self, i: int, j: int):
        if self.exploration_grid[i][j] != "reported":
            print("This place wasn't reported")
            return
        
        self.exploration_grid[i][j] = "nothing"
    
    def is_explosed(self) -> bool:
        return self.is_explosed
    
    def get_near_mines(self, i: int, j: int) -> int:
        sum = 0

        for add_i in range(-1, 2):
            for add_j in range(-1, 2):
                if i + add_i in range(self.dimensions[0]) and j + add_j in range(self.dimensions[1]):
                    sum += self.mines_grid[i + add_i][j + add_j]
        
        return sum
    
    def display_grid(self):
        print("=" * self.dimensions[1] + "\n" * 2)
        for i in range(self.dimensions[0]):
            line = ""
            for j in range(self.dimensions[1]):

                match self.exploration_grid[i][j]:
                    case "nothing":
                        line += " "
                    
                    case "reported":
                        line += "X"
                    
                    case "explored":
                            line += str(self.get_near_mines(i, j))

                line += " "
            
            print(line)