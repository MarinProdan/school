from grid1 import Grid

grid = Grid("grid_02.json")
grid.print()

for i in range(4):
    grid.rotate()
    print("---")
    grid.print()