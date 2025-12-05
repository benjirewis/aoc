testfile = './inputs/real.txt'

class Grid():
    grid: list[list[int]]

    def __init__(self, file_lines: list[str]):
       self.grid = [[1 if c == '@' else 0 for c in line] for line in file_lines] 

    def __str__(self) -> str:
        return '\n'.join(''.join('.@x'[cell] for cell in row) for row in self.grid)

    def is_accessible_via_forklift(self, target_i: int, target_j: int) -> bool:
        num_rolls_adjacent = 0
        # Iterate on a subgrid of 3*3 and use max and min not to run over edges.
        for i in range(max(0, target_i-1), min(target_i-1 + 3, len(self.grid))):
            for j in range(max(0, target_j-1), min(target_j-1 + 3, len(self.grid[0]))):
                if i == target_i and j == target_j:
                    continue
                if self.grid[i][j] == 1 or self.grid[i][j] == 2:
                    num_rolls_adjacent += 1
        return num_rolls_adjacent < 4

    # Transforms grid to mark appropriate rolls with 'x'. Also returns the number of 'x'
    # rolls found.
    def transform(self) -> int:
        num_x_rolls_found = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] == 1 and self.is_accessible_via_forklift(i, j):
                    self.grid[i][j] = 2
                    num_x_rolls_found += 1
        return num_x_rolls_found

with open(testfile, 'r') as file:
    grid = Grid(file.readlines())
    print(grid)
    print('\nNumber of forklift-accessible rolls:', grid.transform(), '\n')
    print(grid)
