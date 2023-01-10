import random


class Deminer:
    
    def __init__(self, dimensions: tuple[int], mine_percentage: int):
        self.dimensions = dimensions
        self.mines_grid = self.generate_mines_grid(mine_percentage)
        self.exploration_grid = self.generate_exploration_grid()
        self.is_explosed = False

        self.first_exploration()

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
    
    def first_exploration(self):
        empty_places = []
        
        for i in range(self.dimensions[0]):
            for j in range(self.dimensions[1]):
                if not self.mines_grid[i][j] and self.get_near_mines(i, j) == 0:
                    empty_places.append((i, j))

        chosen_place = random.choice(empty_places)
        self.explore(chosen_place[0], chosen_place[1])
    
    def explore(self, i: int, j: int):
        if self.exploration_grid[i][j] == "reported":
            print("This place is reported, if you want to explore it you must unreport it before")
            return

        if self.mines_grid[i][j]:
            self.is_explosed = True
            print("Explosion !!")
            return
        
        self.exploration_grid[i][j] = "explored"

        if self.get_near_mines(i, j) == 0:
            for add_i in range(-1, 2):
                for add_j in range(-1, 2):
                    if i + add_i in range(self.dimensions[0]) and j + add_j in range(self.dimensions[1]):
                        if self.exploration_grid[i + add_i][j + add_j] != "explored":
                            self.explore(i + add_i, j + add_j)
    
    def report_mine(self, i: int, j: int):
        self.exploration_grid[i][j] = "reported"
    
    def cancel_report(self, i: int, j: int):
        if self.exploration_grid[i][j] != "reported":
            print("This place wasn't reported")
            return
        
        self.exploration_grid[i][j] = "nothing"
    
    def is_explosed(self) -> bool:
        return self.is_explosed
    
    def result(self) -> int:
        if self.is_explosed():
            return -1
        
        is_correct = True
        for i in range(self.dimensions[0]):
            for j in range(self.dimensions[1]):
                if self.exploration_grid[i][j] == "nothing":
                    return 0

                if self.exploration_grid[i][j] == "reported" and self.mines_grid[i][j] == 0:
                    is_correct = False
        
        if is_correct:
            return 1
        
        else:
            return -1
    
    def get_near_mines(self, i: int, j: int) -> int:
        sum = 0

        for add_i in range(-1, 2):
            for add_j in range(-1, 2):
                if i + add_i in range(self.dimensions[0]) and j + add_j in range(self.dimensions[1]):
                    sum += self.mines_grid[i + add_i][j + add_j]
        
        return sum
    
    def display_grid(self):
        print("   " + " ".join([str(j) for j in range(self.dimensions[1])]) + "\n   " + "=" * self.dimensions[1] * 2)

        for i in range(self.dimensions[0]):
            line = f"{i} |"
            for j in range(self.dimensions[1]):

                match self.exploration_grid[i][j]:
                    case "nothing":
                        line += " "
                    
                    case "reported":
                        line += "X"
                    
                    case "explored":
                            line += str(self.get_near_mines(i, j))

                line += " "
            
            print(line + "|")
        
        print("   " + "=" * self.dimensions[1] * 2)