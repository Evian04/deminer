import random


class Deminer:
    
    def __init__(self, dimensions: list[int], mine_percentage: int):
        self.dimensions = dimensions
        self.mines_grid = self.generate_grid(mine_percentage)
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