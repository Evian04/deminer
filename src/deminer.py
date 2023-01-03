import random


class Deminer:
    
    def __init__(self, dimensions: list[int], mine_percentage: int):
        self.dimensions = dimensions
        self.grid = self.generate_grid(mine_percentage)
    
    def generate_grid(self, percentage: int) -> list[list[int]]:
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